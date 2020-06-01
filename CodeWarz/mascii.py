#!/usr/bin/env python3

def convert(val):
	if val.startswith('0x'):
		return chr(int(val[2:], 16))
	if val.startswith('0b'):
		return chr(int(val[2:], 2))
	if val.startswith('0'):
		return chr(int(val[1:], 8))
	return chr(int(val))

ans = []
for val in open(__import__('sys').argv[1], 'r').read().strip().split():
	ans.append(convert(val))
print(''.join(ans[:-1]), end='')