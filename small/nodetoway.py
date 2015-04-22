# nodetoway.py (nodedict version)

import pickle
import xml.etree.ElementTree as ET

output = open('nodedict.txt','rb')
nodedict = pickle.load(output)

tree = ET.parse('small.osm')
root = tree.getroot()
ways = root.findall('way')

for way in ways:
    nds = way.findall('nd')
    for nodeid in nodedict:
        for nd in nds:
            if int(nd.attrib['ref']) == nodeid:
                print nodeid,nd.attrib['ref']
                for crime in nodedict[nodeid]:
                    print crime
                    ET.SubElement(way,'tag',{'crime':crime})

tree.write('smallway.osm')