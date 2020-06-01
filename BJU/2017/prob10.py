word = input().lower()
num = 1
while word != 'end':
	l = []
	while word != 'last':
		l.append(word)
		word = input().strip().lower()

	l.sort()
	total = 0
	for i in range(len(l) - 1):
		total += 1
		for x, y in zip(l[i], l[i+1	]):
			if x != y:
				break
			else:
				total += 1
	print('List {} has Webster ranking = {}'.format(num, total + len(l)))
	num += 1
	word = input().strip().lower()