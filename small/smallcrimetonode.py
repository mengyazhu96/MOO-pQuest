# nodetoway.py
#
# takes in an OSM file (command line input), inserts a crime parameter into NODES and outputs an [XML OR OSM] file

import xml.etree.ElementTree as ET
import pickle
import sys

# get dictionary of crime data
output = open('smalldict.txt', 'rb')
crimedict = pickle.load(output)
# maybe separate into separate dictionaries?

tree = ET.parse('small.osm')
root = tree.getroot()

def comp_coords(crime,osm):
    return abs(crime - osm) < 10 ** -6

for child in root:
    if child.tag == 'node':
        # get coordinates of node
        lat = float(child.attrib['lat'])
        lon = float(child.attrib['lon'])
        for (lati,longi),val in crimedict.items():
            # compare approxes and exacts of coordinates
            if int(lati) == int(lat) and int(longi) == int(lon):
                if comp_coords(lati,lat) and comp_coords(longi,lon):
                    for crime in val:
                        ET.SubElement(child,'tag',{'crime':crime['CR']})
                        # should we stop the loop? (break)
                
tree.write('smallcrime.osm')