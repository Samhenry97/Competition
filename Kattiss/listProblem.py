n = int(input())

l = list()
cur = 1
l.append(cur)
total = cur
found = False
while not found:
	while total > n:
		total //= l[0]
		del l[0]
	print(total)
	if total == n:
		found = True
	cur += 1
	total *= cur
	l.append(cur)

print(len(l))
