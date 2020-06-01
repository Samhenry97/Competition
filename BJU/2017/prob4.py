i = int(input())
while i != -1:
	l = list(map(int, input().split()))
	grid = []
	for item in l:
		tmp = bin(item)[2:]
		if len(tmp) < i:
			tmp = '0' * (i - len(tmp)) + tmp
		grid.append(tmp)

	maxHor = 0
	hor = 0
	horStart = False
	for item in grid:
		if hor > maxHor:
			maxHor = hor
		hor = 0
		horStart = False
		for c in item:
			if c == '1':
				if horStart:
					hor += 1
				else:
					hor = 1
					horStart = True
			elif c == '0':
				horStart = False
				if hor > maxHor:
					maxHor = hor
				hor = 0
	if hor > maxHor:
		maxHor = hor

	maxVer = 0
	ver = 0
	verStart = False
	for x in range(i):
		if ver > maxVer:
			maxVer = ver
		ver = 0
		verStart = False
		for y in range(i):
			if grid[y][x] == '1':
				if verStart:
					ver += 1
				else:
					ver = 1
					verStart = True
			elif grid[y][x] == '0':
				verStart = False
				if ver > maxVer:
					maxVer = ver
				ver = 0
	if ver > maxVer:
		maxVer = ver

	if maxVer == maxHor:
		print(maxVer, 'both')
	elif maxVer > maxHor:
		print(maxVer, 'vertical')
	else:
		print(maxHor, 'horizontal')

	i = int(input())