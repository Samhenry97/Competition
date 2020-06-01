#!/usr/bin/env python3


data = open(__import__('sys').argv[1], 'r').read()
ans = []
for word in data.split():
	beg = []
	end = []
	flag = False
	for c in word:
		if flag: beg.append(c)
		else: end.append(c)
		flag = not flag
	ans.append(''.join(beg) + ''.join(end[::-1]))
print('twisted: {}'.format(data))
print('plain  : {}'.format(' '.join(ans)), end='')