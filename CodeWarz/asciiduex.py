#!/usr/bin/env python3

def decode(s):
	val = sum([ord(c) for c in s])
	print(val)

first = False
for line in open(__import__('sys').argv[1], 'r'):
	if first: print()
	first = True
	ans = []
	for word in line.split():
		ans.append(decode(word))
	print(''.join(ans), end='')