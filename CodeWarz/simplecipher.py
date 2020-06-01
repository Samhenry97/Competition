#!/usr/bin/env python3

ans = []
last = True
for val in open(__import__('sys').argv[1], 'r').read().strip().split():
	if last:
		ans.append(val)
		last = False
	else:
		last = '.' in val
print(' '.join(ans), end='')