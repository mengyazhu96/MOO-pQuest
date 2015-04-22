# nodetoway.py
#
# DATA PROCESSING STEP 3
# 
# takes in our nodedict and matches nodes to the ways they are in, inserting crimes into 
#     a way if a crime node is in it; returns our final OSM data, smallway.osm
#
# final product: 
#     <way blahblahblah>
#        <nd ref='the node id'>
#            and the rest of its nodes
#        <tag uselesstags>
#        <tag crime='CRIME TYPE'>
#        <tag crime='CRIME TYPE'>
#     </way>

import pickle
import xml.etree.ElementTree as ET

# open our nodedict
output = open('nodedict.txt','rb')
nodedict = pickle.load(output)

# get all the ways from our OSM data set
tree = ET.parse('small.osm')
root = tree.getroot()
ways = root.findall('way')

# iterate through the ways
for way in ways:
    
    # get all the nodes in the way
    nds = way.findall('nd')
    
    # iterate through the nodes with crime in the nodedict
    for nodeid in nodedict:
        
        # check each crime node against the nodes in the way
        for nd in nds:
            if int(nd.attrib['ref']) == nodeid:
                
                # if the node ids match, add a crime tag to the way for each crime at the node
                for crime in nodedict[nodeid]:
                    ET.SubElement(way,'tag',{'crime':crime})

# write to our final OSM file
tree.write('smallway.osm')