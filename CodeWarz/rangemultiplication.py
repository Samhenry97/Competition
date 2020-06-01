#!/usr/bin/env python3

first = False
for line in open(__import__('sys').argv[1], 'r'):
	if first: print()
	first = True
	a, b, c = map(int, line.split())
	ans = []
	for i in range(a, c):
		if i % a == 0 and i % b == 0:
			ans.append(i)
	print(ans, end='')