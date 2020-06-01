import sys
sys.setrecursionlimit(10000)

dp = {0: 0, 1: 1}

def calc(n):
	if n in dp:
		return dp[n]
	parts = n // 2, n // 3, n // 4
	total = sum([calc(x) for x in parts])
	dp[n] = max(total, n)
	return dp[n]

for line in sys.stdin:
	print(calc(int(line)))