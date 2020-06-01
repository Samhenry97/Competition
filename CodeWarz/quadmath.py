#!/usr/bin/env python3
from decimal import Decimal

first = False
for line in open(__import__('sys').argv[1], 'r'):
	if first: print()
	first = True
	data = line.split()
	if len(set(data)) == 1:
		if '.' not in line:
			ans = str(sum(list(map(int, data))) * 4)
		else:
			ans = str(sum(list(map(float, data))) * 4.0)
	else:
		if '.' not in line:
			ans = str(sum(list(map(int, data))))
		else:
			ans = str(sum(list(map(float, data))))
	print(ans, end='')