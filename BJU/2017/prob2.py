l = []

i, w = input().split()
i = int(i)
while i and w != '-':
	l.append((i, w))
	i, w = input().split()
	i = int(i)
l.sort()

i = int(input())
while i:
	ans = []
	for item in l:
		if i % item[0] == 0:
			ans.append(item[1])
	if len(ans) > 0:
		print(''.join(ans))
	else:
		print(i)
	i = int(input())