import re

r = re.compile(r'^(\+|-)?[0-9]+(((\.[0-9]+)((E|e)(\+|-)?[0-9]+)?)|((E|e)(\+|-)?[0-9]+))$')

s = input().strip()
while s != '*':
	print(s, 'is', ['illegal.', 'legal.'][bool(r.match(s))])
	s = input().strip()