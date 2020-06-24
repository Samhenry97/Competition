n, m = map(int, input().split())
grid = []
total = n * m * 2
for y in range(n):
    grid.append(list(map(int, input().split())))
    for x in range(m):
        total += (int(y == 0) + int(y == n - 1) + int(x == 0) + int(x == m - 1)) * grid[y][x]
        
for y in range(n):
    for x in range(m):
        cur = grid[y][x]
        if x > 0:
            total += max(grid[y][x - 1] - cur, 0)
        if y > 0:
            total += max(grid[y - 1][x] - cur, 0)
        if x + 1 < m:
            total += max(grid[y][x + 1] - cur, 0)
        if y + 1 < n:
            total += max(grid[y + 1][x] - cur, 0)
print(total)