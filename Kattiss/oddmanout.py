n = int(input())

for i in range(n):
	input()
	l = list(map(int, input().split()))
	d = {}
	for pos in l:
		if pos in d: d[pos] += 1
		else: d[pos] = 1
	for elem in d:
		if d[elem] == 1:
			print("Case #" + str(i + 1) + ": " + str(elem))
