n, q = map(int, input().split())
l = [input() for i in range(n)]
for i in range(q):
	s = input()
	count = 0
	ans = ''
	for saying in l:
		if saying.startswith(s):
			ans = saying
			count += 1
	if count == 0:
		print('No chapel sayings.')
	elif count == 1:
		print(ans)
	else:
		print('Multiple chapel sayings.')