h, n = map(int, input().split())
while h or n:
	if h == 1 and n == 1: 
		print(0, 1)
	else:
		m = 1
		while h != int((n ** ((1/m) + 1.0)) ** m + 1e-8): m += 1
		total = int(n ** (1/m) + 1e-8)
		if n != 1: print(int((1-n)/(1-total)), (h - n) * total + h)
		else: print(m, (h - n) * total + h)

	h, n = map(int, input().split())