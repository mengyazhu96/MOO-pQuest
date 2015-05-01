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
from loadOsm import LoadOsm

# defines a float comparison function: each of the latitude and longitude coordinates
#    must be within 10^-4 degrees (about 0.0069 miles or 36 feet), so within a 
#    36ft by 36ft square
def comp_coords(cords,osm):
    return abs(cords - osm) < 10 ** -4

def cordtonode(lat, lon, data):
	node_data = LoadOsm(data)
	return node_data.findNode(lat, lon, 'foot')


