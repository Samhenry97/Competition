l = [1]
max = 10 ** 60
finished = False
while not finished:
	print(*l)
	new = [1]
	for i in range(1, len(l)):
		new.append(l[i] + l[i - 1])
		if new[-1] >= max:
			finished = True
	new.append(1)
	l = new[:]
print(*l)