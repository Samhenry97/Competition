#!/usr/bin/env python3
from decimal import Decimal

first = False
for line in open(__import__('sys').argv[1], 'r'):
	if first: print()
	first = True
	data = line.strip().split()
	if len(data) == 2:
		a, b = data
		try:
			ans = Decimal(a) + Decimal(b)
			print(__import__('re').sub('\.0+$', '', str(ans)), end='')
		except:
			first = False
	else:
		first = False