#!/usr/bin/env python3

data = [int(line) for line in open(__import__('sys').argv[1], 'r')]
ans = []
for i in range(len(data) // 2):
	ans.append(str(data[i] + data[-i - 1]))
if len(data) & 1: ans.append(str(data[len(data) // 2]))
print(', '.join(ans), end='')