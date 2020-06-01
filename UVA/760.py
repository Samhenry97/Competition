first = True
while True:
	try:
		if not first: print()
		else: first = False
		dna1, dna2 = input(), input()
		ans = set()
		longest = 0
		for i in range(len(dna1)):
			for j in range(len(dna2)):
				if dna1[i] == dna2[j]:
					test1 = i + 1
					test2 = j + 1
					while test1 < len(dna1) and test2 < len(dna2) and dna1[test1] == dna2[test2]:
						test1 += 1
						test2 += 1
					diff = test1 - i
					if diff > longest:
						longest = diff
						ans.clear()
						ans.add(dna1[i:test1])
					elif diff == longest:
						ans.add(dna1[i:test1])
		if longest != 0:
			print('\n'.join(sorted(ans)))
		else:
			print('No common sequence.')

		input()
	except EOFError:
		break