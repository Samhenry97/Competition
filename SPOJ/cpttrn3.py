for _ in range(int(input())):
	n, m = map(int, input().split())
	for y in range(n):
		print('***' * m + '*')
		print('*..' * m + '*')
		print('*..' * m + '*')
	print('***' * m + '*')
	print()