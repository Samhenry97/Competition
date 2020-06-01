#!/usr/bin/env python3

first = False
for line in open(__import__('sys').argv[1], 'r'):
	if first: print()
	first = True
	ans = []
	a, b = map(int, line.split())
	for i in range(a, b+1):
		if i % 7 == 0 and i % 5 != 0:
			ans.append(str(i))
	print(','.join(ans), end='')