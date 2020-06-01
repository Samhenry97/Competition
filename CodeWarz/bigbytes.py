#!/usr/bin/env python3
from sys import argv

with open(argv[1], 'r') as file:
	bits = file.read().strip()

ans = []
for rep in range(0, len(bits), 8):
	ans.append(chr(int(bits[rep:rep+8], 2)))
print(''.join(ans))