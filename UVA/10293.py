import re

while True:
	try:
		s = ''
		tmp = input()
		while tmp != '#':
			if len(s) and s[-1] == '-':
				s += tmp
			else:
				s += ' ' + tmp
			tmp = input()
		res = re.split(r"[^a-zA-Z'-]", s)
		freq = {}
		for word in res:
			word = ''.join([c for c in word if c.isalpha()])
			l = len(word)
			if l:
				freq[l] = freq[l] + 1 if l in freq else 1
		for i in range(31):
			if i in freq:
				print(i, freq[i])
		print()
	except EOFError:
		break