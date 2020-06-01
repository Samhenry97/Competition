n = int(input())
while n:
	names = input().split()
	net = { name: 0 for name in names }
	for _ in range(n):
		data = input().split()
		amt = int(data[1])
		give = int(data[2])
		for name in data[3:]:
			net[name] += amt // give
		if give == 0:
			net[data[0]] -= amt
		else:
			net[data[0]] -= amt // give * give
	for name in names:
		print(name, net[name])
	print()
	n = int(input())