#!/usr/bin/env python3
from sys import argv
from decimal import Decimal
import re

first = False
for line in open(argv[1], 'r'):
	try:
		if first: print('\n')
		first = True

		ans = []
		div, top = map(lambda x: abs(Decimal(x)), line.split())
		cur = div
		while cur <= top:
			if cur >= 1:
				tmp = re.sub('\.0+$', '', str(cur))
				if '.' not in tmp:
					ans.append(tmp)
			cur += div
		print('\n'.join(ans), end='')
	except:
		pass