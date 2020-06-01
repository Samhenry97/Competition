#!/usr/bin/env python3
from functools import cmp_to_key

m = {}
total = 0
for line in open(__import__('sys').argv[1], 'r'):
	for c in line.strip():
		c = c.lower()
		if c.isalnum() or c == ' ':
			m[c] = m[c] + 1 if c in m else 1
			total += 1
data = []
for k, v in m.items():
	data.append((v, k))
for el in sorted(data, key=cmp_to_key(lambda x, y: x[0] - y[0] if x[0] != y[0] else ord(y[1]) - ord(x[1])), reverse=True):
	print("'{}' {}%".format(el[1], round(el[0] / total * 100, 2)))