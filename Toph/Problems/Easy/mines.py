n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]
delta = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
for y in range(n):
    for x in range(m):
        if grid[y][x] == '*':
            continue
        cnt = 0
        for dy, dx in delta:
            yy, xx = y + dy, x + dx
            if 0 <= yy < n and 0 <= xx < m and grid[yy][xx] == '*':
                cnt += 1
        if cnt != 0:
            grid[y][x] = str(cnt)
for i in range(n):
    print(''.join(grid[i]))