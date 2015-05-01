import cPickle as pickle

# the default CrimeWeights dictionary: these numbers may not make complete sense
# lower number = avoiding more
CrimeWeights = {   
    'GRAND LARCENY': 0.6,
    'FELONY ASSAULT': 0.6,
    'ROBBERY': 0.8,
    'GRAND LARCENY OF MOTOR VEHICLE': 0.95,
    'BURGLARY': 0.95,
    'RAPE': 0.45,
    'MURDER': 0.4
}

# modifies the default CrimeWeights dictionary to reflect:
#	n: user input of safety importance
# 	ignores: user inputs of crime types to ignore
def weight_crime(n,ignores):
    # if the user inputs with the ranges
	if n > 1 and n <= 10:
		crime_factor = (10.1 - n) / 10.1
		for k,v in CrimeWeights.items():
			print v, v*crime_factor
			CrimeWeights[k] = v * crime_factor
	else:
		if n != 1:
			print "Invalid input, not using crimes."
		# if the user inputs 1, then safety does not matter at all so we won't use crime
		else:
			print "Not using crime."
        # renders the CrimeWeights dictionary ineffective
		for k in CrimeWeights:
			CrimeWeights[k] == 1

    # ignores all the given crimes
	for ignore in ignores:
		ignore_crime(ignore)

	# open a file and pickle.dump the dictionary there
	output = open('crimeweights.txt', 'ab+')
	pickle.dump(CrimeWeights, output)
	output.close()

# sets a crimetype weight to be 1, rendering its weight meaningless
def ignore_crime(crimetype):
	if crimetype.upper() in CrimeWeights:
		CrimeWeights[crimetype.upper()] = 1