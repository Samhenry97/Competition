for t in range(int(input())):
	if t != 0: print()
	input()

	freq = {}
	for c in input():
		if c.isalpha():
			freq[c] = freq[c] + 1 if c in freq else 1
	freq = sorted([(f, c) for c, f in freq.items()], reverse=True)

	e = input()
	code = {}
	for c in e:
		code[c] = code[c] + 1 if c in code else 1
	code = sorted([(f, c) for c, f in code.items()], reverse=True)

	alg = {}
	for i in range(len(freq)):
		alg[code[i][1]] = freq[i][1]

	ans = []
	for c in e:
		ans.append(alg[c])
	print(''.join(ans))