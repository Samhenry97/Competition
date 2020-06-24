delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
n = int(input())
grid = [list(map(int, list(input()))) for _ in range(n)]
ans = [[str(grid[y][x]) for x in range(n)] for y in range(n)]
for y in range(1, n-1):
    for x in range(1, n-1):
        if all([grid[y + dy][x + dx] < grid[y][x] for dy, dx in delta]):
            ans[y][x] = 'X'
for y in range(n):
    print(''.join(ans[y]))