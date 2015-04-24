# crimetonode2.py (nodedict version - see junk for other)
#
# DATA PROCESSING STEP 2
# 
# takes in an OSM file, gets the nodes from that file, and then creates a dictionary
#    that relates a node to a crime using the node's lat/long and the crime's lat/long
#
# final product: nodedict[nodeid] = [list of crimes (only their types)]

import xml.etree.ElementTree as ET
import pickle
import sys

# get our crime data dictionary
output = open('smalldict.txt', 'rb')
crimedict = pickle.load(output)

# get all the nodes from our OSM data set
tree = ET.parse('small.osm')
root = tree.getroot()
nodes = root.findall('node')

# initialize our output dictionary
nodedict = {}

# defines a float comparison function: each of the latitude and longitude coordinates
#    must be within 10^-4 degrees (about 0.0069 miles or 36 feet), so within a 
#    36ft by 36ft square
def comp_coords(crime,osm):
    return abs(crime - osm) < 10 ** -4

# iterate through all the nodes in our OSM data
for node in nodes:
    
    # get the id and coordinates of node
    id = node.attrib['id']
    lat = float(node.attrib['lat'])
    lon = float(node.attrib['lon'])
    
    # initialize a list of crimes for this node
    crimelist = []
    
    # iterate through the crimedict
    for (lati,longi),val in crimedict.items():
        
        # compare coordinates
        if comp_coords(lati,lat) and comp_coords(longi,lon):
            
            # iterate through all the crimes at that point and add them to 
            #    the node's crimelist
            for crime in val:
                crimelist.append(crime['CR'])
                
    # if the crimelist is not empty, then that means there were crimes at that
    #    node and so we must store it in our nodedict
    if crimelist:
        nodedict[id] = crimelist

# pickle.dump the nodedict into a file
output = open('nodedict.txt', 'ab+')
pickle.dump(nodedict, output)
output.close()

# next step: nodetoway.py