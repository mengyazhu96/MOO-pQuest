# MOO-pQuest Usage Instructions

Testing Notes
-------------
OSM data is often very inefficient, as is PyRoute. We have provided you with three data files: small.osm, smallway.osm, and manway.osm. The first of these, smallway.osm, is the processed version of small.osm, and these two files only contain 100th-120th streets in Manhattan. All of Manhattan with crime parameters is contained in manway.osm; we did not give you the origin file for Manhattan because (a) it is very large and (b) it took a very long time to run.

Data Processing
---------------
From within the MOO-pQuest folder, run python process.py [path/to/osm/file] [path/to/new/osm/file]. The same effect can be achieved in multiple steps by using smalldict.py, crimetonode.py, and nodetoway.py (in that order) using the command line arguments detailed within each file. Within data/small are examples of the .txt outputs that are created through this process.

Routing
-------
From within the pyroute subfolder, run python execute.py [path/to/processed/osm]. You will then be met with a series of prompts detailing:
1. crime types (optional)
2. safety importance on a scale of 1 to 10
3. start and end addresses
4. maximum distance to walk (optional)

Reasons for failing may include:
* typos in the input addresses (3)
* not providing a number for safety importance (2)
* not typing crime types exactly (1)
* (4) is greater than the distance traversed by the calculated path, but not greater than the absolute distance between the origin and destination

Note that failing to meet the specifications for the prompts will result in that parameter being ignored. Also note that the address input will map to the nearest routeable node, and so may not be completely accurate.