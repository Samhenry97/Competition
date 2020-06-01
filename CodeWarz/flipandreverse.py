#!/usr/bin/env python3

ans = []
flag = False
for line in open(__import__('sys').argv[1], 'r'):
	for word in line.split():
		ans.append(word[::-1] if flag else word)
		flag = not flag
print('\n'.join(ans), end='')