# execute.py
# 
# combines pieces (loadOsm, Router, gen_dict) into final command-line execution
#
# command line arguments: 1) OSM file to use 2) start node id 3) end node id

import sys
import subprocess
from gen_dict import *
from math import sin, cos, atan2, sqrt, pi

# calculates the distance in miles between two lat lon coordinates
def dist_miles(start,end):
	start_lat = start[0]
	start_lon = start[1]
	end_lat = end[0]
	end_lon = end[1]

	dlat = abs(end_lat - start_lat) * (pi / 180)
	dlon = abs(end_lon - start_lon) * (pi / 180)

	a = (sin(dlat / 2.0))**2 + (cos(end_lat * (pi / 180)) * cos(start_lat * (pi / 180)) * (sin(dlon / 2.0))**2)
	c = 2.0 * atan2(sqrt(a), sqrt(1.0 - a))
	return (3963.1676) * c

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
start = int(sys.argv[2])
end = int(sys.argv[3])
result, route = router.doRouteAsLL(start, end, 'foot')

abs_dist = dist_miles(router.coords(start),router.coords(end))

print "Your destination is {} miles away".format(abs_dist)
dist_input = raw_input('Please enter, in miles, the maximum distance you want to traverse (leave blank if unnecessary): ')
max_dist = None
if dist_input == '':
	print 'Not accounting for distance.'
elif abs_dist > float(dist_input):
	print 'Input distance less than absolute distance between nodes. Ignoring distance input.'
else:
	max_dist = float(dist_input)

# print out the results
if result == 'success':
	# compute distance
	distance = 0.0
	for i in range(len(route) - 1):
		distance += dist_miles(route[i],route[i+1])

	if (max_dist is None) or max_dist > distance:
		print
		print "Route: %s" % ",".join("%1.4f,%1.4f" % (i[0],i[1]) for i in route)
		print
		print "Distance traveled: {} miles".format(distance)
	else:
		print "Could not find short enough route."

else:
	print "Failed (%s)" % result

# remove the pickle-dumped text file after use
subprocess.call(["rm","crimeweights.txt"])