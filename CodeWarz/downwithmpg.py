#!/usr/bin/env python3
from sys import argv

ans = []
longest = 0
for i in range(1, len(argv)):
	firstPast = False
	pStart, pStop, pGal, pCar = 0, 1, 2, 3
	for line in open(__import__('sys').argv[i], 'r'):
		if firstPast:
			data = [x.strip() for x in line.strip().split(',')]
			longest = max(longest, len(data[pCar]))
			ans.append([data[pCar], '{}'.format((float(data[pStop]) - float(data[pStart])) / float(data[pGal]))])
		else:
			data = [x.strip() for x in line.strip().split(',')]
			try: pStart = data.index('miles_start')
			except: pass
			try: pStop = data.index('miles_stop')
			except: pass	
			try: pGal = data.index('gallons')
			except: pass
			try: pCar = data.index('car')
			except: pass
			firstPast = True
print('\n'.join(' '.join([x[0].rjust(longest), str(x[1])]) for x in ans), end='')