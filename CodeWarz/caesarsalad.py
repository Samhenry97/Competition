#!/usr/bin/env python3
ans = []
for line in open(__import__('sys').argv[1], 'r'):
	tmp = []
	rot = 0
	for word in line.split():
		decoded = []
		for c in word:
			if c.isupper():
				newVal = ord(c) - ord('A') - rot
				if newVal < 0: newVal += 26
				newVal += ord('A')
			elif c.islower():
				newVal = ord(c) - ord('a') - rot
				if newVal < 0: newVal += 26
				newVal += ord('a')
			else:
				newVal = ord(c)
			decoded.append(chr(newVal))
		rot += 1
		tmp.append(''.join(decoded))
	ans.append(' '.join(tmp))

print('\n'.join(ans), end='')