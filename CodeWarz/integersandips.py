#!/usr/bin/env python3

def convert(num):
	return '{}.{}.{}.{}'.format((num >> 24), (num >> 16) & 0xFF, (num >> 8) & 0xFF, num & 0xFF)

first = False
for line in open(__import__('sys').argv[1], 'r'):
	if first: print()
	first = True
	ans = []
	for word in line.split():
		try:
			if '.' in word: raise
			num = int(word)
			ip = convert(num)
			if ip[0] == '0': raise
			ans.append(ip)
		except:
			ans.append(word)
	print(' '.join(ans), end='')