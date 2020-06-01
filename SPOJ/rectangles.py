from math import sqrt, floor

n = int(input())

max = floor(sqrt(n))
ans = 0
for i in range(1, max+1):
	test = i
	while i * test <= n:
		ans += 1
		test += 1

print(ans)