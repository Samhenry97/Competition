d = {}

while True:
	s = input()
	if s == '':
		break
	s = s.split()
	d[s[1]] = s[0]

while True:
	try:
		s = input()
		if s in d: print(d[s])
		else: print("eh")
	except EOFError:
		break
