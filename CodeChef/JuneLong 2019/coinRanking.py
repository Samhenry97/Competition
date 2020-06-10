for _ in range(int(input())):
	u, v = map(int, input().split())
	print(((u + v) * (u + v + 1)) // 2 + 1 + u)