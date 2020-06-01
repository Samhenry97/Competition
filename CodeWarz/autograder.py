#!/usr/bin/env python3
from sys import argv
from os import walk

students = {}
grades = {}
for root, dirs, files in walk(argv[1]):
	if len(files):
		fname = files[0]
		num = int(fname.lstrip('student').rstrip('_comments'))
		with open(root + '/' + fname, 'r') as grade:
			for line in grade:
				line = line.strip()
				data = line.split('|')
				if len(data) == 5 and 'maximum' not in line:
					grades[num] = int(data[3].replace('%', '')) if num not in grades else grades[num] + int(data[3].replace('%', ''))
					students[num] = line if num not in students else students[num] + '\n' + line
first = False
for student in sorted(students.keys()):
	if first: print('\n')
	first = True
	print('student{}'.format(student))
	print(students[student])
	print('Total: {}%'.format(grades[student]), end='')