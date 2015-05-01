# nodetoway.py
#
# DATA PROCESSING STEP 3
# 
# takes in our nodedict and matches nodes to the ways they are in, inserting crimes into 
#     a way if a crime node is in it; returns our final OSM data, smallway.osm
#
# command line inputs: 1) node dictionary dump file 2) OSM data set 3) output OSM file
#           for small: 1) nodedict.txt              2) small.osm    3) smallway.osm
#
# final product: 
#     <way blahblahblah>
#        <nd ref='the node id'>
#            and the rest of its nodes
#        <tag uselesstags>
#        <tag k = 'crime' v = 'CRIME TYPE id'>
#     </way>

import cPickle as pickle
import xml.etree.ElementTree as ET
import sys

# open our nodedict
output = open(sys.argv[1],'rb')
nodedict = pickle.load(output)

# get all the ways from our OSM data set
tree = ET.parse(sys.argv[2])
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
tree.write(sys.argv[3])