for _ in range(int(input())):
	n = int(input())
	good = True
	for num in list(map(int, input().split()))[1:]:
		if n % num != 0:
			good = False
			break
	print('{} - {}.'.format(n, ['Simple', 'Wonderful'][good]))