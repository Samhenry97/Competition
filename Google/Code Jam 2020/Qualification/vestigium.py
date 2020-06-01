for tc in range(int(input())):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    rotgrid = list(zip(*grid))
    trace = sum([grid[i][i] for i in range(n)])
    row = sum([int(len(set(grid[i])) != n) for i in range(n)])
    col = sum([int(len(set(rotgrid[i])) != n) for i in range(n)])
    print('Case #{}:'.format(tc+1), trace, row, col)