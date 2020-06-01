r, c = map(int, input().split())

grid = []
for y in range(r):
    grid.append([c for c in input()])

for x in range(c):
    ground = r - 1
    for y in range(r - 1, -1, -1):
        if grid[y][x] == '#':
            ground = y - 1
        elif grid[y][x] == 'o':
            grid[y][x] = '.'
            grid[ground][x] = 'o'
            ground -= 1
for y in range(r):
    print(''.join(grid[y]))
