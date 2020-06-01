for _ in range(int(input())):
	n, m, r, c = map(int, input().split())
	for y in range(n):
		print(('*' * (c + 1)) * m + '*')
		for x in range(r):
			print(('*' + '.' * c) * m + '*')
	print(('*' * (c + 1)) * m + '*')
	print()