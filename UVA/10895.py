while True:
	try:
		m, n = map(int, input().split())
		mat = [[0 for i in range(n)] for i in range(m)]
		for row in mat:
			indices = list(map(lambda x: int(x) - 1, input().split()[1:]))
			data = list(map(int, input().split()))
			for i, idx in enumerate(indices):
				row[idx] = data[i]

		mat = list(zip(*mat))
		print(len(mat), len(mat[0]))
		for row in mat:
			indices = [i + 1 for i in range(len(row)) if row[i] != 0]
			data = [row[i - 1] for i in indices]
			print(len(indices), *indices)
			print(*data)
	except EOFError:
		break