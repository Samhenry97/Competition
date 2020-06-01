from math import sqrt

def sieve(n):
	prime = [True] * (n + 1)

	for i in range(2, int(sqrt(n)) + 1):
		test = i * 2
		while test < n:
			prime[test] = False
			test += i

	return prime

twins = set()
p = sieve(120000)
test = 3
while test < len(p) - 2:
	if p[test] and p[test + 2]:
		twins.add(test)
		twins.add(test + 2)
	test += 1

twins = sorted(list(twins))
sums = set()
for y in range(len(twins)):
	for x in range(y, len(twins)):
		sums.add(twins[y] + twins[x])
		
ans = sorted(list(sums))
for _ in range(int(input())):
	print(ans[int(input()) - 1])