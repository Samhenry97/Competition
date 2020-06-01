#!/usr/bin/env python3

first = False
for line in open(__import__('sys').argv[1], 'r'):
	if first: print()
	first = True
	a, b = map(int, line.split())
	print(sum([x for x in range(min(a, b), max(a, b) + 1)]), end='')