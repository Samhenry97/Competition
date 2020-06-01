input()
l = list(map(int, input().split()))
tot = 0
for i, n in enumerate(l):
	tot += l[i]
	print(tot/(i+1))