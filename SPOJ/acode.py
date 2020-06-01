line = input()
while line != '0':
	dp = [0] * len(line)
	dp[0] = 1
	for i in range(1, len(line)):
		if line[i] != '0':
			dp[i] = dp[i - 1]
		if 9 < int(line[i-1] + line[i]) < 27:
			if i == 1:
				dp[i] += 1
			else:
				dp[i] += dp[i - 2]
	print(dp[-1])
	line = input()