#!/usr/bin/env python3
import re

valid = re.compile('^(\d{1,3}\.){3}\d{1,3}')

class IP:
	def __init__(self, octs, str):
		self.octs = octs
		self.count = 1
		self.str = str

	def __lt__(self, other):
		if self.count != other.count:
			return self.count < other.count
		return self.octs < other.octs

ips = {}
for line in open(__import__('sys').argv[1], 'r'):
	if valid.search(line):
		ip = valid.search(line).group(0)
		octs = [int(x) for x in ip.split('.')]
		if all([x <= 255 for x in octs]):
			if ip in ips:
				ips[ip].count += 1
			else:
				ips[ip] = IP(octs, ip)
first = False
for ip in sorted(ips.values(), reverse=True):
	if first: print()
	first = True
	print('{}: {} ({})'.format(ip.str.rjust(15), '*' * ip.count, ip.count), end='')