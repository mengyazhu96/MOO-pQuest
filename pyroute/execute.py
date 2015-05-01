# execute.py
# 
# combines pieces into final command-line execution

import sys
import subprocess
from gen_dict import *

execfile('gen_dict.py')

safety_input = int(raw_input('Please enter safety importance on a scale of 1 to 10: '))
weight_crime(safety_input)

from route import Router
from loadOsm import *

data = LoadOsm(sys.argv[1])


router = Router(data)
result, route = router.doRouteAsLL(int(sys.argv[2]), int(sys.argv[3]), 'foot')

if result == 'success':
	print "Route: %s" % ",".join("%1.4f,%1.4f" % (i[0],i[1]) for i in route)
else:
	print "Failed (%s)" % result

subprocess.call(["rm","crimeweights.txt"])