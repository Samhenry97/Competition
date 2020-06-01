#!/usr/bin/env python3

ans = []
for line in open(__import__('sys').argv[1], 'r'):
	idx = int(line.split()[0]) - 1
	data = list(map(int, line.split()[1].split(','))) * 2
	for i in range(idx, len(data)):
		if data[i] > data[idx]:
			ans.append(str(data[i]))
			break
print('\n'.join(ans), end='')