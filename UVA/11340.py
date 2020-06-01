for _ in range(int(input())):
	cost = {}
	for _ in range(int(input())):
		c, v = input().split()
		cost[c] = int(v)
	total = 0
	for _ in range(int(input())):
		for c in input():
			if c in cost:
				total += cost[c]
	print('{0:.2f}$'.format(total / 100))