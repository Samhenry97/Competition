#!/usr/bin/env python3

delta = [(-1, 0), (0, -1), (1, 0), (0, 1)]

with open(__import__('sys').argv[1], 'r') as file:
	n = int(file.readline())
	grid = [list(file.readline().strip()) for y in range(n)][::-1]
	vis = [[-1 for x in range(n)] for y in range(n)]
vis[0][0] = 0
q = [(0, 0)]
while len(q):
	y, x = q[0]
	del q[0]
	for dy, dx in delta:
		newy, newx = y + dy, x + dx
		if 0 <= newy < n and 0 <= newx < n and vis[newy][newx] == -1 and grid[newy][newx] == 'O':
			q.append((newy, newx))
			vis[newy][newx] = vis[y][x] + 1
print(vis[-1][-1] if vis[-1][-1] != -1 else 'Puzzle cannot be solved!')
