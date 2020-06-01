while True:
	try:
		l = list(map(int, input().split()[1:]))
		diff = set([abs(l[i] - l[i - 1]) for i in range(1, len(l))])
		print(['Not jolly', 'Jolly'][len(diff) == len(l) - 1 and (len(diff) == 0 or (min(diff) == 1 and max(diff) == len(l) - 1))])
	except EOFError:
		break