#!/usr/bin/env python3
import re
from decimal import Decimal

ans = Decimal('0')
for line in open(__import__('sys').argv[1], 'r'):
	for val in line.split(','):
		try:
			ans += Decimal(val)
		except Exception as e:
			pass
print(re.sub('\.0+$', '', str(ans)), end='')