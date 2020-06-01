while True:
	try:
		seq = list(map(int, input().split()))[:-1]
		prod = [0] * len(seq)
		prod[0] = seq[0]
		for i in range(1, len(seq)):
			prod[i] = prod[i-1] * seq[i]
		ans = prod[-1]
		for y in range(1, len(prod)):
			for x in range(y+1, len(prod)):
				test = prod[x] // prod[y-1]
				if test > ans:
					ans = test
		print(ans)
	except EOFError:
		break