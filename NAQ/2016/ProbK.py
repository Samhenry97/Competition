def poss(a,b,c):
	ans = []
	for x in range(1, c):
		if (c - x * a) % b == 0 and (c - x * a) // b >= 1:
			ans.append((x, (c - x * a) // b))
	return ans

for i in range(int(input())):
	a,b,c,d,e,f = map(int, input().split())
	top = e * b - f * a
	bot = c * b - d * a
	if len(poss(a + b, c + d, e + f)) == 1:
		x, y = poss(a + b, c + d, e + f)[0]
		print(x, y)
	elif bot == 0 or top % bot != 0:
		print("?")
	else:
		m = top // bot
		top = e - m * c
		bot = a
		if bot == 0 or top % bot != 0:
			print("?")
		else:
			n = top // bot
			if n > 0 and m > 0:
				print(n, m)
			else:
				print("?")