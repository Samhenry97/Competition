#!/usr/bin/env python3

from decimal import Decimal

names = []
data = []
first = True
for line in open(__import__('sys').argv[1], 'r'):
	if first:
		names = [x.strip() for x in line.split(',')]
		data = [Decimal('0')] * len(line.split(','))
		first = False
	for i, part in enumerate(line.split(',')):
		part = part.strip()
		try: data[i] += Decimal(part)
		except: pass
print(','.join(names))
print(','.join([str(x) for x in data]), end='')	