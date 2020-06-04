def search(t):
    global grid
    for y in range(3):
        if grid[y].count('X') >= 2:
            return t
    rgrid = list(zip(*grid))
    for y in range(3):
        if rgrid[y].count('X') >= 2:
            return t
    if [grid[x][x] for x in range(3)].count('X') >= 2:
        return t
    if [grid[x][-x-1] for x in range(3)].count('X') >= 2:
        return t
        
    ans = 0
    for y in range(3):
        for x in range(3):
            if grid[y][x] == '.':
                grid[y][x] = 'X'
                ans = max(ans, search(t+1))
                grid[y][x] = '.'
    return ans

for i in range(int(input())):
    grid = [list(input()) for _ in range(3)]
    t = grid[0].count('X') + grid[1].count('X') + grid[2].count('X')

    for y in range(3):
        assert(grid[y].count('X') != 3) 
    rgrid = list(zip(*grid))
    for y in range(3):
        assert(rgrid[y].count('X') != 3)
    assert([grid[x][x] for x in range(3)].count('X') != 3)
    assert([grid[x][-x-1] for x in range(3)].count('X') != 3)

    print('Game #{}: {}'.format(i+1, ['Alice', 'Bob'][search(t)%2]))