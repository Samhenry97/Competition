n = int(input())
ans = []
total = 0
for i in range(n):
	s = input()
	total += (n - i) * (i + 1)
	ans.append('{} {}'.format((n - i) * (i + 1), s))
print(total)
print('\n'.join(ans))