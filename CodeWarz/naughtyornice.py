#!/usr/bin/env python3
import re

good = bad = 0
for line in open(__import__('sys').argv[1], 'r'):
	good += bool(line.strip().endswith('good'))
	bad += bool(line.strip().endswith('bad'))
print('Naughty list has {} people!'.format(bad))
print('Nice list has {} people!'.format(good), end='')