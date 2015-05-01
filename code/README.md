# MOO-pQuest

Navigational tools do not address the safety of a given route. When walking in New York City, a tool like Google Maps will provide the most efficient route, but it will not account for the safety of the given path.

To fix this problem, we plan on integrating historical crime data with open source map navigation technology to generate a route-calculating algorithm that will account for path safety. We hope to develop an effective navigation tool for New York City that will take parameters for safety in determining efficient walking directions.

This is a final project for CS51.

Code and Data Acknowledgments
-----------------------------
* OSM data from https://www.openstreetmap.org.
* Crime data from http://maps.nyc.gov/crime/, extracted to JSON format from http://thomaslevine.com/!/nyc-crime-map/.
* Routing algorithm is Pyroute, https://wiki.openstreetmap.org/wiki/Pyroute.

Algorithm Breakdown
-------------------
* Crime data is in crimedata.geojson. We parse this into a Python dictionary in parsedata.py, which outputs crimedict.txt (in pickle format). 
* This dictionary is then read into insertcrime.py, which adds a crime tag to either nodes or ways (unimplemented). OSM data (small test area) is in data.osm. insertcrime.py parses the OSM data through the ElementTree XML API.
* We then modify Pyroute to account for the new weights (pyroute/weights.py).

