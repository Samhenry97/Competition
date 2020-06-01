def find(x):
    par = x
    while disjoint[par] >= 0: 
        par = disjoint[par]
    if par != x: disjoint[x] = par
    return par

def merge(x, y):
    parx, pary = find(x), find(y)

    if parx == pary: return
    if disjoint[parx] < disjoint[pary]:
        disjoint[pary] += disjoint[parx]
        disjoint[parx] = pary
    else:
        disjoint[parx] += disjoint[pary]
        disjoint[pary] = parx

deltas = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
n, m = map(int, input().split())
disjoint = [-1] * (n * m)

grid = [list(input()) for _ in range(n)]
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == '#':
            for dx, dy in deltas:
                xx, yy = x + dx, y + dy
                if xx >= 0 and xx < m and yy >= 0 and yy < n and grid[yy][xx] == '#':
                    merge(y * m + x, yy * m + xx)
print(sum([1 for x in disjoint if x < -1]))