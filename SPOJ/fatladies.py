for _ in range(int(input())):
	i = int(input())
	if (i - 1) % 4 == 0:
		print(i // 4 * 1000 + 192)
	elif (i - 1) % 4 == 1:
		print(i // 4 * 1000 + 442)
	elif (i - 1) % 4 == 2:
		print(i // 4 * 1000 + 692)
	else:
		print((i // 4 - 1) * 1000 + 942)