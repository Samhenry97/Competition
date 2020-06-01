#!/usr/bin/env python3
import re

first = False
for line in open(__import__('sys').argv[1], 'r'):
	if first: print()
	first = True
	print(sum(list(map(lambda x: int(x[2:], 16), line.split()))), end='')