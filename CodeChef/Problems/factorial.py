def calcZeros(x):
	ans = 0
	n = 5 ** 13
	while x > n:
		n /= 5
	while n >= 5:
		ans += x // n
		n /= 5
	return int(ans)

for _ in range(int(input())):
	print(calcZeros(int(input())))