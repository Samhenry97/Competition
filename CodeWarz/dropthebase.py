#!/usr/bin/env python3
import base64
from sys import argv

def findMatch(code):
	with open('/usr/share/dict/american-english', 'r') as words:
		for word in words:
			word = word.strip()

			test = base64.b64encode(word.encode('utf-8')).decode('utf-8').strip().replace('=', '')
			while len(test) <= len(code) * 2:
				if test == code:
					print(word, end='')
					return
				test = base64.b64encode(test.encode('utf-8')).decode('utf-8').strip().replace('=', '')

with open(argv[1], 'r') as file:
	found = False
	for line in file:
		if found:
			print()
		findMatch(line.strip())
		found = True