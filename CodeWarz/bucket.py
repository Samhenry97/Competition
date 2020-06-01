#!/usr/bin/env python3
from sys import argv

buckets = [0] * 10000
largest = 0
for line in open(argv[1], 'r'):
	line = line.strip()
	group = int(line) // 10
	largest = max(group, largest)
	buckets[group] += 1
print(''.join(list(map(str, buckets[:largest+1]))), end='')