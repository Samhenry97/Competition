for _ in range(int(input())):
	n, m = map(int, input().split())
	print('*' * m)
	for i in range(n - 2):
		print('*' + ('.' * (m - 2)) + '*' if m > 1 else '*')
	if n > 1:
		print('*' * m)
	print()