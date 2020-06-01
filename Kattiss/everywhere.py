n = int(input())

for i in range(n):
	d = dict()
	total = int(input())
	for m in range(total):
		city = input()
		if city in d:
			d[city] += 1
		else:
			d[city] = 1
	print(len(d))
