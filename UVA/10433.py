while True:
	try:
		n = input().strip()
		sn = str(int(n) ** 2)
		print(['Automorphic number of {}-digit.'.format(len(n)), 'Not an Automorphic number.'][n in ['0', '1'] or sn.find(n, len(sn) - len(n)) == -1])
	except EOFError:
		break