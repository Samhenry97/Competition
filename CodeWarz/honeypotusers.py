#!/usr/bin/env python3
import os, sys, re
from functools import cmp_to_key

# 2016-11-29 07:46:02-0500 [CowrieTelnetTransport,663,185.73.144.18] login attempt [admin/admin] succeeded
loginRegex = re.compile('\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}-\d{4} \[[^\[]*\] login attempt \[([^/]*)/([^/]*)\]')
userData = {}

dir = sys.argv[1]
for fName in os.listdir(dir):
	for line in open(dir + '/' + fName, 'r', errors='ignore'):
		match = loginRegex.match(line.strip())
		if match:
			user = match.group(1)
			pwd = match.group(2)
			if user not in userData:
				userData[user] = {}
			userData[user][pwd] = userData[user][pwd] + 1 if pwd in userData[user] else 1

def userCmp(u1, u2):
	c1 = sum(userData[u1].values())
	c2 = sum(userData[u2].values())
	if c1 != c2: return c1 - c2
	else: return [1, -1][[(v, k) for k, v in userData[u1].items()] < [(v, k) for k, v in userData[u2].items()]]

def pwdCmp(p1, p2):
	if p1[1] != p2[1]: return p1[1] - p2[1]
	else: return [1, -1][p1[0] < p2[0]]

for uName in sorted(userData.keys(), key=cmp_to_key(userCmp)):
	print('User account "{}" has been attempted "{}" times overall.'.format(uName, sum(userData[uName].values())))
	for k, v in sorted(userData[uName].items(), key=cmp_to_key(pwdCmp)):
		print('    Password "{}" was attempted {} times.'.format(k, v))