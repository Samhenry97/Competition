def check(grids, win): 
	ans = False
	for i, grid in enumerate(grids):
		for y in range(5):
			if grid[y].count(True) == 5:
				if not win[i]: 
					print('Card {} wins with a horizontal bingo!'.format(i + 1))
					ans = True
					win[i] = True
		tmp = list(zip(*grid))
		for y in range(5):
			if tmp[y].count(True) == 5:
				if not win[i]: 
					print('Card {} wins with a vertical bingo!'.format(i + 1))
					ans = True
					win[i] = True
		count = 0
		count2 = 0
		for c in range(5):
			if grid[c][c]:
				count += 1
			if grid[-c-1][-c-1]:
				count2 += 1	
		if count == 5 or count2 == 5:
			if not win[i]: 
				print('Card {} wins with a diagonal bingo!'.format(i + 1))
				ans = True
				win[i] = True
	return ans

inp = list(map(int, input().split()))
while True:
	try:
		inp.extend(list(map(int, input().split())))
	except EOFError:
		break

games = []
while 0 in inp:
	idx = inp.index(0)
	games.append(inp[:idx])
	inp = inp[idx+1:]

for game in games:
	n = game[0]
	game = game[1:]

	cards = []
	grids = []
	win = [False] * n
	for i in range(n):
		grids.append([])
		for y in range(5):
			grids[i].append([])
			for x in range(5):
				grids[i][y].append(False)

	for i in range(n):
		cards.append({})
		nums = game[:25]
		game = game[25:]
		for y in range(5):
			for x in range(5):
				cards[i][nums[y * 5 + x]] = (y, x)

	output = True
	for el in game:
		for i in range(len(cards)):
			if el in cards[i]:
				pos = cards[i][el]
				grids[i][pos[0]][pos[1]] = True
		if check(grids, win):
			output = False
	if output:
		print('No winner!')

	if n == 1:
		break