# smalldict.py
#
# DATA PROCESSING STEP 1
# 
# uses the same methodology as ../parsecrime.py to generate a crime dictionary
#     limited to our input OSM file, small.osm
# command line inputs: 1) OSM file with bounds 2) name of .txt file to be outputted
#             for us:    small.osm                smalldict.txt

import json
import cPickle as pickle
import xml.etree.ElementTree as ET
import sys

# open the geoJSON file
with open('../crimedata.geojson') as data_file:    
    data = json.load(data_file)

# set up command line arguments
osm = sys.argv[1]
txt = sys.argv[2] 

# parse the OSM file for its boundaries
tree = ET.parse(osm)
bounds = tree.getroot()[0].attrib
minlat = float(bounds['minlat'])
maxlat = float(bounds['maxlat'])
minlon = float(bounds['minlon'])
maxlon = float(bounds['maxlon'])

# initialize our dictionary
crimedict = {}
crimes = data['features']

# iterate through the geoJSON data
for i in range(len(crimes)):
    crime = crimes[i]

    # A crime has geometry, type, and properties
    # type: always Feature, can ignore
    # geometry: includes coordinates of the point: DOES [LONG, LAT] (counterintuitive)
    # properties: MO (month), TOT (total?), X, Y, CR (crime type), YR (year)
    # CR can be: MURDER, RAPE, ROBBERY, FELONY ASSAULT, BURGLARY, GRAND LARCENY, 
    #     GRAND LARCENY OF MOTOR VEHICLE
    
    # gets lat/long coordinates - note that they are backwards
    pos = (crime['geometry']['coordinates'][1],crime['geometry']['coordinates'][0])
    
    # checks to see that this crime is within our bounds
    if pos[0] >= minlat and pos[0] <= maxlat and pos[1] >= minlon and pos[1] <= maxlon:
        
        # gets the dictionary of the crime's properties
        properties = crime['properties']
        properties['id'] = i
        
        # if this coordinate is already in our dict (if more than one crime has occurred here)
        if pos in crimedict:
            val = crimedict[pos]
            val.append(properties)
            crimedict[pos] = val
        else:
            crimedict[pos] = [properties]

# open a file with the given title and pickle.dump the dictionary there
output = open(txt, 'ab+')
pickle.dump(crimedict, output)
output.close()

# next step: crimetonode.py