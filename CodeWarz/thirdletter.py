#!/usr/bin/env python3

first = False
for line in open(__import__('sys').argv[1], 'r'):
	if first: print()
	first = True
	ans = []
	for word in line.split():
		if len(word) > 2:
			ans.append(word[1:3] + word[0] + word[3:])	
		else:
			ans.append(word)
	print(' '.join(ans), end='')