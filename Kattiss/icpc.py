from math import log

ops, n, t = map(int, input().split())

made = True
if t == 1:
	cur = n - 1
	while cur > 1:
		n *= cur
		cur -= 1
		if n > ops:
			made = False
			break
elif t == 2:
	if 2 ** n > ops:
		made = False
elif t == 3:
	if n ** 4 > ops:
		made = False
elif t == 4:
	if n ** 3 > ops:
		made = False
elif t == 5:
	if n * n > ops:
		made = False
elif t == 6:
	if n * log(n, 2) > ops:
		made = False
elif t == 7:
	if n > ops:
		made = False

if made:
	print("AC")
else:
	print("TLE")
