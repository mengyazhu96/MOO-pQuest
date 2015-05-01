# execute.py
# 
# combines pieces (loadOsm, Router, gen_dict) into final command-line execution
#
# command line arguments: 1) OSM file to use 2) start node id 3) end node id

import sys
import subprocess
from gen_dict import *

# parse user specification of crime types to ignore
for k in CrimeWeights:
	print k

ignore_input = raw_input("Please select crime types from above to ignore (if any), separated by commas: ")
ignore = [i.strip() for i in ignore_input.split(',')]

print

# parse user specification of safety importance
safety_input = int(raw_input('Please enter safety importance on a scale of 1 to 10: '))

# call the weight_crime function from gen_dict to modify the crimedict used in loadOsm
weight_crime(safety_input,ignore)

print

# these have to be loaded in later, because route depends on loadOsm 
#	which depends on the modified crimeweights dictionary
from route import Router
from loadOsm import *

# load in the given OSM file
data = LoadOsm(sys.argv[1])

# do the routing
router = Router(data)
result, route = router.doRouteAsLL(int(sys.argv[2]), int(sys.argv[3]), 'foot')

# print out the results
if result == 'success':
	print "Route: %s" % ",".join("%1.4f,%1.4f" % (i[0],i[1]) for i in route)
else:
	print "Failed (%s)" % result

# remove the pickle-dumped text file after use
subprocess.call(["rm","crimeweights.txt"])