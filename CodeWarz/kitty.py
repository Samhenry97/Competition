#!/usr/bin/env python3
from sys import argv

with open(argv[1], 'r') as file:
	print(file.read())