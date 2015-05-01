# cordtonode.py
# 
# 
# Takes in a lat long coordinate and outputs a node ID which correponds
# 
# 
# 
# 


import xml.etree.ElementTree as ET
import sys
import pickle



#lat = sys.argv[1]
#lon = sys.argv[2]

# get all the nodes from our OSM data set
#tree = ET.parse(sys.acrgv[1])
#root = tree.getroot()
#nodes = root.findall('node')


# defines a float comparison function: each of the latitude and longitude coordinates
#    must be within 10^-4 degrees (about 0.0069 miles or 36 feet), so within a 
#    36ft by 36ft square
def comp_coords(cords,osm):
    return abs(cords - osm) < 10 ** -4

def make_node(lat, lon, nodes):
	for node in nodes:
		id = node.attrib['id']
		lat1 = float(node.attrib['lat'])
		lon1 = float(node.attrib['lon'])

		if comp_coords (lat, lat1) and comp_coords(lon, lon1):
			#check if it is part of a way.
			if (node != None):
				return id
			else:
				for tag in node:
					if tag.attrib['k'] == 'highway':
						return id    
	#raise an error
	print "Error: Address not within bounds. Please pick an address in Manhattan"



