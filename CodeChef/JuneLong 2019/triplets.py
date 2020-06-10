for _ in range(int(input())):
	a, b, c = map(int, input().split())
	p = [int(x) for x in input().split()]
	q = [int(x) for x in input().split()]
	r = [int(x) for x in input().split()]

	p.sort()
	q.sort(reverse=True)
	r.sort()

	sum = 0

	ai = 0
	while ai < a:
		bi = 0
		while bi < b and p[ai] <= q[bi]:
			ci = 0
			curSum = p[ai] + q[bi]
			while ci < c and q[bi] >= r[ci]:
				sum += curSum  * (q[bi] + r[ci])
				ci += 1
			bi += 1
		ai += 1

	print(sum % 1000000007)
	