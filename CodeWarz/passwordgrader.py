#!/usr/bin/env python3
from sys import argv

with open(argv[1], 'r') as file:
	first = False
	for line in file:
		if first: print()
		first = True

		line = line.strip()
		upper, lower, number, other = 0, 0, 0, 0
		for c in line:
			if c.isupper(): upper += 1
			elif c.islower(): lower += 1
			elif c.isdigit(): number += 1
			else: other += 1
		failed = int(len(line) > 20) + int(len(line) < 8) + int(upper == 0) + int(lower == 0) + int(number == 0) + int(other == 0)
		print('Password:', '({})'.format(str(len(line)).rjust(2, '0')), line.ljust(20)[:20], ' Status:', ['Failed {} check{}'.format(failed, ['s', ''][failed == 1]), 'Passed all checks!'][failed == 0], end='')