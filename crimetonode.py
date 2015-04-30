# crimetonode.py (nodedict version - see junk for other)
#
# DATA PROCESSING STEP 2
# 
# takes in an OSM file, gets the nodes from that file, and then creates a dictionary
#    that relates a node to a crime using the node's lat/long and the crime's lat/long
#
# command line inputs: 1) crime dictionary dump file 
#                        2) OSM data set 3) output dictionary dump file
# for small: 1) smalldict.txt 2) small.osm 3) nodedict.txt
#
# final product: nodedict[nodeid] = [list of crimes (only their types)]

import xml.etree.ElementTree as ET
import pickle
import sys


# get our crime data dictionary
output = open(sys.argv[1], 'rb')
crimedict = pickle.load(output)

# get all the nodes from our OSM data set
tree = ET.parse(sys.argv[2])
root = tree.getroot()
nodes = root.findall('node')

# initialize our output dictionary
nodedict = {}

# defines a float comparison function: each of the latitude and longitude coordinates
#    must be within 10^-4 degrees (about 0.0069 miles or 36 feet), so within a 
#    36ft by 36ft square
def comp_coords(crime,osm):
    return abs(crime - osm) < 10 ** -4

# iterate through the crimedict
for (lati,longi),val in crimedict.items():

    # iterate through all the nodes in our OSM data
    for node in nodes:
    
        # get the id and coordinates of node
        id = node.attrib['id']
        lat = float(node.attrib['lat'])
        lon = float(node.attrib['lon'])
    
        # compare coordinates
        if comp_coords(lati,lat) and comp_coords(longi,lon):
            
            if id in nodedict:
                for crime in val:
                    nodedict[id].append((crime['CR'],crime['id']))

            else:
                nodedict[id] = []
                for crime in val:
                    nodedict[id].append((crime['CR'],crime['id']))

# pickle.dump the nodedict into a file
output = open(sys.argv[3], 'ab+')
pickle.dump(nodedict, output)
output.close()

# next step: nodetoway.py