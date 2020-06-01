#!/usr/bin/env python3
from sys import argv
from math import log

nums = [u'\u2080', u'\u2081', u'\u2082', u'\u2083', u'\u2084', u'\u2085', u'\u2086', u'\u2087', u'\u2088', u'\u2089']

def unicodeBase(base):
	ans = []
	for c in str(base):
		ans.append(nums[ord(c) - ord('0')])
	return ''.join(ans)

with open(argv[1], 'r') as file:
	error = True
	for line in file:
		if not error: print()
		error = False

		try:
			maxTest, base, ans = map(int, line.split())
			if base ** ans < maxTest:
				print('log{}({}) = {}'.format(unicodeBase(base), base ** ans, ans), end='')
			else:
				print('ERROR!: log{}(x) = {} Could not be solved'.format(unicodeBase(base), ans), end='')
		except Exception as e:
			error = True