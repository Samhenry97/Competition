def gen(grid):
    n, m = len(grid), len(grid[0])
    ans = [['.'] * m for _ in range(n)]
    for y in range(n):
        for x in range(m):
            valid = grid[y][x] != 'O'
            for dy, dx in delta:
                yy, xx = y + dy, x + dx
                if 0 <= yy < n and 0 <= xx < m and grid[yy][xx] == 'O':
                    valid = False
            if valid:
                ans[y][x] = 'O'
    return ans

delta = [(0, 1), (0, -1), (-1, 0), (1, 0)]
n, m, t = map(int, input().split())
gridOne = [list(input()) for _ in range(n)]
gridThree = gen(gridOne)
gridFive = gen(gridThree)

if t == 1:
    for y in range(n):
        print(*gridOne[y], sep='')
elif t % 4 == 1:
    for y in range(n):
        print(*gridFive[y], sep='')
elif t % 4 == 3:
    for y in range(n):
        print(*gridThree[y], sep='')
else:
    for y in range(n):
        print('O' * m)
