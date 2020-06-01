while True:
	try:
		n, s = input().split()
		n = int(n)

		freq = {}
		for i in range(len(s) - n + 1):
			tmp = s[i:i+n]
			freq[tmp] = freq[tmp] + 1 if tmp in freq else 1
		m = max(freq.values())
		for k, v in freq.items():
			if v == m:
				print(k)
				break
	except EOFError:
		break