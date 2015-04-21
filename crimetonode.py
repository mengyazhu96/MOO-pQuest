# nodetoway.py
#
# takes in an OSM file, inserts a crime parameter into NODES and outputs an [XML OR OSM] file

import xml.etree.ElementTree as ET
import pickle

# read data
output = open('crimedict.txt', 'rb')
crimedict = pickle.load(output)    # 'obj_dict' is a dict object

tree = ET.parse('data.osm')
root = tree.getroot()

for child in root:
    if child.tag == 'way':
        #insert crime paramater
    #potentially get rid of superfluous info, e.g. usernames