#!/usr/bin/env python3

ans = []
for line in open(__import__('sys').argv[1], 'r'):
	data = line.split(',')
	if len(data) == 1:
		try: ans.append(int(line))
		except: pass
	elif len(data):
		tmp = []
		for num in data:
			try: tmp.append(int(num))
			except: pass
		if len(tmp):
			ans.append(tmp)

print(ans, end='')