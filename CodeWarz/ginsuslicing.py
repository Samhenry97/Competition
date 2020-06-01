#!/usr/bin/env python3

ans = []
for line in open(__import__('sys').argv[1], 'r'):
	tmp = []
	for word in line.split():
		dec = word[:len(word)//2][::-1]
		if len(word) & 1:
			dec += word[len(word)//2]
			dec += word[len(word)//2+1:][::-1]
		else:
			dec += word[len(word)//2:][::-1]
		tmp.append(dec)
	ans.append(' '.join(tmp))
print('\n'.join(ans), end='')