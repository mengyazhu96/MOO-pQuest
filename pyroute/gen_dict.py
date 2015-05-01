import cPickle as pickle

CrimeWeights = {   
    'GRAND LARCENY': 0.7,
    'FELONY ASSAULT': 0.7,
    'ROBBERY': 0.8,
    'GRAND LARCENY OF MOTOR VEHICLE': 0.9,
    'BURGLARY': 0.9,
    'RAPE': 0.5,
    'MURDER': 0.5
}

def weight_crime(n):
	if n > 1 and n <= 10:
		crime_factor = (10.1 - n) / 10.1
		for k,v in CrimeWeights.items():
			print v, v*crime_factor
			CrimeWeights[k] = v * crime_factor
	else:
		print "Not using crime."
		if n != 1:
			print "Invalid input, not using crimes."
		for k in CrimeWeights:
			CrimeWeights[k] == 1

	# open a file and pickle.dump the dictionary there
	output = open('crimeweights.txt', 'ab+')
	pickle.dump(CrimeWeights, output)
	output.close()
	return CrimeWeights