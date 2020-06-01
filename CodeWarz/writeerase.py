#!/usr/bin/env python3
from sys import argv
import re, socket

regex = re.compile('CWN\{.+\}')

s = socket.socket()
s.connect((argv[1], int(argv[2])))
ans = s.recv(2048)
while len(ans) > 0:
	ans = ans.decode('utf-8').strip()
	if regex.match(ans):
		print(regex.match(ans).group(0), end='')
	ans = s.recv(2048)