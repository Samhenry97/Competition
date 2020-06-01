for _ in range(int(input())):
	n, m = map(int, input().split())
	for i in range(n):
		opt = '*.' if i % 2 else '.*'
		print(''.join([opt[0] if j % 2 else opt[1] for j in range(m)]))