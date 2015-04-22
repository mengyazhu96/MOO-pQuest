# crimetonode.py (nodedict version)

# outputs dictionary with keys node IDs and values a list of crimes (their types) that have occurred

import xml.etree.ElementTree as ET
import pickle
import sys

# get dictionary of crime data
output = open('smalldict.txt', 'rb')
crimedict = pickle.load(output)

tree = ET.parse('small.osm')
root = tree.getroot()
nodes = root.findall('node')

nodedict = {}

def comp_coords(crime,osm):
    return abs(crime - osm) < 10 ** -4

for node in nodes:
    # get coordinates of node
    id = int(node.attrib['id'])
    lat = float(node.attrib['lat'])
    lon = float(node.attrib['lon'])
    crimelist = []
    for (lati,longi),val in crimedict.items():
        # compare approxes and exacts of coordinates
        if int(lati) == int(lat) and int(longi) == int(lon):
            if comp_coords(lati,lat) and comp_coords(longi,lon):
                for crime in val:
                    crimelist.append(crime['CR'])
    if crimelist:
        nodedict[id] = crimelist
        
output = open('nodedict.txt', 'ab+')

pickle.dump(nodedict, output)
output.close()
