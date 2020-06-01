while True:
	n, m = map(int, input().split())
	if(n is 0 and m is 0): break
	jack = set()
	jill = set()
	for i in range(n):
		jack.add(int(input()))
	for i in range(m):
		jill.add(int(input()))
	final = jack.intersection(jill)
	print(len(final))
