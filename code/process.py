# process.py
#
# DATA PROCESSING: combined into one
# 
# combines the functionality of smalldict.py, crimetonode.py, and nodetoway.py
#	to hopefully cut down run time by not dealing with pickle-dumping dictionaries
#
# command line inputs: 1) original OSM file 2) name of OSM file to be outputted
#      e.g. for small:    small.osm            smallway.osm

import json
import xml.etree.ElementTree as ET
import sys

# set up command line arguments
osm = sys.argv[1]

# parse the OSM file
tree = ET.parse(osm)
root = tree.getroot()


"""CONSOLIDATE THE CRIME DATA TO THE BOUNDS OF OUR FILE"""
# open the geoJSON file
with open('../data/crimedata.geojson') as data_file:    
    data = json.load(data_file)

# get the boundaries of the OSM data
bounds = root[0].attrib
minlat = float(bounds['minlat'])
maxlat = float(bounds['maxlat'])
minlon = float(bounds['minlon'])
maxlon = float(bounds['maxlon'])

# initialize our restricted dictionary
crimedict = {}
crimes = data['features']

# iterate through the geoJSON data to restrict the data we process
for i in range(len(crimes)):
    crime = crimes[i]

    # gets lat/long coordinates - note that they are backwards
    pos = (crime['geometry']['coordinates'][1],crime['geometry']['coordinates'][0])
    
    # checks to see that this crime is within our bounds
    if pos[0] >= minlat and pos[0] <= maxlat and pos[1] >= minlon and pos[1] <= maxlon:
        
        # gets the dictionary of the crime's properties
        properties = crime['properties']

        # assign each unique crime an id
        properties['id'] = i
        
        # if this coordinate is already in our dict (if more than one crime has occurred here)
        if pos in crimedict:
            val = crimedict[pos]
            val.append(properties)
            crimedict[pos] = val
        else:
            crimedict[pos] = [properties]


"""ASSIGN CRIMES TO NODES"""
# get all the nodes in the OSM data
nodes = root.findall('node')

# initialize our node-crime dictionary
nodedict = {}

# defines a float comparison function: each of the latitude and longitude coordinates
#    must be within 10^-4 degrees (about 0.0069 miles or 36 feet), so within a 
#    36ft by 36ft square
def comp_coords(crime,osm):
    return abs(crime - osm) < 10 ** -4

# iterate through the (restricted) crimedict
for (lati,longi),val in crimedict.items():

    # iterate through all the nodes in our OSM data
    for node in nodes:
    
        # get the id and coordinates of node
        id = node.attrib['id']
        lat = float(node.attrib['lat'])
        lon = float(node.attrib['lon'])
    
        # compare coordinates
        if comp_coords(lati,lat) and comp_coords(longi,lon):
            
            # if this node is already in our output dictionary
            if id in nodedict:
                for crime in val:
                	# list of tuples of crimes (crimetype,id)
                    nodedict[id].append((crime['CR'],crime['id']))

            else:
            	# otherwise we need to initialize the list
                nodedict[id] = []
                for crime in val:
                    nodedict[id].append((crime['CR'],crime['id']))
                    

"""PUT CRIMES IN WAYS"""
# get al the ways in the OSM file
ways = root.findall('way')

# iterate through the ways
for way in ways:
    
    # get all the nodes in the way
    nds = way.findall('nd')
    
    # iterate through the nodes with crime in the nodedict
    for nodeid in nodedict:
        
        # check each crime node against the nodes in the way
        for nd in nds:
            if nd.attrib['ref'] == nodeid:
                
                # if the node ids match, add a crime tag to the way for each crime at the node
                for crime in nodedict[nodeid]:
                    crimetag = crime[0] + ' ' + str(crime[1])
                    
                    # checks to make sure exact crime not in tags already
                    tags = way.findall('tag')
                    repeat = False
                    for tag in tags:
                        if tag.attrib['v'] == crimetag:
                            repeat = True
                            break

                    if not repeat:
                        ET.SubElement(way,'tag',{'k':'crime','v': crimetag})

# write to our final OSM file
tree.write(sys.argv[2])