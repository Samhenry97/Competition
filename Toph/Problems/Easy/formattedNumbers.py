s = input()[::-1]
a = []
for i, c in enumerate(s):
	if i != 0 and i % 3 == 0:
		a.append(',')
	a.append(c)
print(''.join(a[::-1]))