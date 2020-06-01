def calc(a, b):
	k = 1
	while True:
		top = int(1e8)
		bottom = 0
		n = top >> 1
		while top - bottom > 1:
			ans = (n + 1) ** k
			if ans == a and n ** k == b:
				count = 1
				for i in range(1, k):
					count += n ** (k - i)
				height = a
				curHeight = a
				levelTotal = 1
				for i in range(k):
					curHeight //= n + 1
					levelTotal *= n
					height += curHeight * levelTotal
				return (count, height)
			elif ans > a:
				top = n
			else:
				bottom = n
			n = (top + bottom) >> 1
		k += 1

a, b = map(int, input().split())
while a or b:
	if a == 1:
		print(0, 1)
	else:
		print(*calc(a, b))
	a, b = map(int, input().split())
