#!/usr/bin/env python3
from functools import reduce
from operator import mul
from decimal import Decimal
import re

ans = []
for line in open(__import__('sys').argv[1], 'r'):
	ans.append(str(reduce(mul, list(map(Decimal, line.split())), 1)))
print('\n'.join(ans))