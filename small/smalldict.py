# filters the dictionary to only look at the bounds within a given OSM file.
# command line inputs: 1) OSM file with bounds 2) name of .txt file to be outputted

import json
import pickle
import xml.etree.ElementTree as ET
import sys

with open('../crimedata.geojson') as data_file:    
    data = json.load(data_file)

osm = sys.argv[1]
txt = sys.argv[2]
tree = ET.parse(osm)
bounds = tree.getroot()[0].attrib
minlat = bounds['minlat']
maxlat = bounds['maxlat']
minlon = bounds['minlon']
maxlon = bounds['maxlon']


crimedict = {}
crimes = data['features']
for crime in crimes:
    # A crime has geometry, type, and properties
    # type: always Feature, can ignore
    # geometry: includes coordinates of the point: DOES [LONG, LAT] (counterintuitive)
    # properties: MO (month), TOT (total?), X, Y, CR (crime type), YR (year)
    # CR can be: MURDER, RAPE, ROBBERY, FELONY ASSAULT, BURGLARY, GRAND LARCENY, 
        # GRAND LARCENY OF MOTOR VEHICLE
    
    # gets the list containing lat/long coordinates - note that they are backwards
    pos = (crime['geometry']['coordinates'][1],crime['geometry']['coordinates'][0])
    print pos,pos[0] >= minlat, pos[0] <= maxlat, pos[1] >= minlon, pos[1] <= maxlon
    if pos[0] >= minlat and pos[0] <= maxlat and pos[1] >= minlon and pos[1] <= maxlon:
        # gets the dictionary of the crime's properties
        properties = crime['properties']
        
        if pos in crimedict:
            val = crimedict[pos]
            val.append(properties)
            crimedict[pos] = val
        else:
            crimedict[pos] = [properties]

print minlat,maxlat,minlon,maxlon
    
#output = open(txt, 'ab+')

#pickle.dump(crimedict, output)
#output.close()