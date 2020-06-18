for _ in range(int(input())):
	input()
	men = sorted(list(map(int, input().split())))
	women = sorted(list(map(int, input().split())))
	print(sum([men[i] * women[i] for i in range(len(men))]))