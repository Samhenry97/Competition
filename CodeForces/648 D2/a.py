for _ in range(int(input())):
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    r, c = set(), set()
    for y in range(n):
        for x in range(m):
            if grid[y][x] == 1:
                r.add(y)
                c.add(x)
    print(['Vivek', 'Ashish'][min(n - len(r), m - len(c)) % 2])