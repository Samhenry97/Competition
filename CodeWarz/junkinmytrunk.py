#!/usr/bin/env python3

ans = []
for line in open(__import__('sys').argv[1], 'r'):
	tmp = []
	for word in line.split():
		idx = len(word) - 1
		while not word[idx].isalpha():
			idx -= 1
		tmp.append(word[:idx] + word[idx+1:])
	ans.append(' '.join(tmp))
print('\n'.join(ans))