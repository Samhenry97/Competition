#!/usr/bin/env python3

ans = []
for line in open(__import__('sys').argv[1], 'r'):
	tmp = []
	for word in line.split():
		subtmp = []
		for subword in word.split('-'):
			subtmp.append(subword[0])
			if len(subword.split('\'')) > 1:
				subtmp.append('\'')
				subtmp.append(subword.split('\'')[1][0])
			if subword[-1] == ',':
				subtmp.append(',')
		tmp.append(''.join(subtmp))
	ans.append(' '.join(tmp))
print('\n'.join(ans), end='')