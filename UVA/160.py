n = int(input())
p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

while n:
	save = n
	dp = [0] * 25
	i = 0
	while n != 1:
		i = n
		j = 0

		while i > 1:
			count = 0
			while i % p[j] == 0:
				i //= p[j]
				count += 1
			dp[j] += count
			j += 1

		n -= 1

	for x in range(24, -1, -1):
		if dp[x] != 0:
			i = x
			break
	j = i
	print(str(save).rjust(3), '! =', end='', sep='')
	flag = [0, 15][j < 15]

	if save != 1:
		for i in range(j+1):
			print(str(dp[i]).rjust(3), end='')
			flag += 1
			if flag == 15:
				flag = 0
				print('\n      ', end='')
	print()

	n = int(input())