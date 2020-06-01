#!/usr/bin/env python3

ans = ''
for line in open(__import__('sys').argv[1], 'r'):
	ans += line.strip('\n')[::-1]
print(ans, end='')