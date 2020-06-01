s = input()

white = 0
lower = 0
upper = 0
symbol = 0
for c in s:
	if c.islower():
		lower += 1
	elif c.isupper():
		upper += 1
	elif c == '_':
		white += 1
	else:
		symbol += 1

print('%.16f' % (white / len(s)))
print('%.16f' % (lower / len(s)))
print('%.16f' % (upper / len(s)))
print('%.16f' % (symbol / len(s)))
