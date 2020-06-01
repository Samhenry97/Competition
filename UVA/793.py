disjoint = []

def find(x):
	par = x
	while disjoint[par] >= 0: par = disjoint[par]
	if par != x: disjoint[x] = par
	return par

def merge(x, y):
	parx, pary = find(x), find(y)

	if parx == pary: return
	if disjoint[parx] < disjoint[pary]:
		disjoint[pary] += disjoint[parx]
		disjoint[parx] = pary
	else:
		disjoint[parx] += disjoint[pary]
		disjoint[pary] = parx

n = int(input())
input()
for _ in range(n):
	disjoint = [-1] * int(input())
	good, bad = 0, 0
	while True:
		try:
			data = input().split()
			while len(data) == 3:
				data[1], data[2] = int(data[1]) - 1, int(data[2]) - 1
				if data[0] == 'c':
					merge(data[1], data[2])
				else:
					if find(data[1]) == find(data[2]):
						good += 1
					else:
						bad += 1
				data = input().split()
			print('{},{}\n'.format(good, bad))
			break
		except EOFError:
			print('{},{}'.format(good, bad))
			break