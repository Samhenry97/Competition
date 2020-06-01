#!/usr/bin/env python3
ans = []
for line in open(__import__('sys').argv[1], 'r'):
	tmp = []
	cap = True
	for word in line.split():
		if cap:
			tmp.append(word.capitalize())
			cap = False
		elif word in list('Ii'):
			tmp.append(word.upper())
		else:
			tmp.append(word.lower())
			cap = '.' in word
	ans.append(' '.join(tmp))

print('\n'.join(ans), end='')