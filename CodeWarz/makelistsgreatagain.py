#!/usr/bin/env python3

first = False
for line in open(__import__('sys').argv[1], 'r'):
	if first: print()
	first = True
	print(str(eval(line)), end='')