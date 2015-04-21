# parsecrime.py
#
# parses geoJSON crime data into a python dictionary, outputted using pickle int crimedict.txt

import json
import pickle

with open('crimedata.geojson') as data_file:    
    data = json.load(data_file)
    
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
    
    # gets the dictionary of the crime's properties
    properties = crime['properties']
    
    if pos in crimedict:
        val = crimedict[pos]
        val.append(properties)
        crimedict[pos] = val
    else:
        crimedict[pos] = [properties]
    # keep CR as string so that we can potentially change their weights later
    
output = open('crimedict.txt', 'ab+')

pickle.dump(crimedict, output)
output.close()