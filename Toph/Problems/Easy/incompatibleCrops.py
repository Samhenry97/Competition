n, m = map(int, input().split())
delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]
grid = [input() for _ in range(n)]
ans = 0
for y in range(n):
    for x in range(m):
        val = grid[y][x] == '.'
        for dy, dx in delta:
            yy, xx = y + dy, x + dx
            if 0 <= yy < n and 0 <= xx < m and grid[yy][xx] == '*':
                val = False
        if val:
            ans += 1
print(ans)