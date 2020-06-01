def calc(h, u, d, f):
	curU, minDist, curH, curDay = u, u * (f / 100), 0, 0

	while(True):
		curDay += 1
		curH += curU
		if curH > h:
			print('success on day {}'.format(curDay))
			return

		curH -= d
		if curH < 0:
			print('failure on day {}'.format(curDay))
			return

		curU -= minDist
		if curU < 0:
			curU = 0

h, u, d, f = map(int, input().split())
while h or u or d or f:
	calc(h, u, d, f)
	h, u, d, f = map(int, input().split())