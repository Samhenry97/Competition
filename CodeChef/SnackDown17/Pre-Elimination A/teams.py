for i in range(int(input())):
	n, m = map(int, input().split())
	n -= m * 2
	for i in range(m):
		input()
	if (n & 1) != 1:
		print("yes")
	else:
		print("no")