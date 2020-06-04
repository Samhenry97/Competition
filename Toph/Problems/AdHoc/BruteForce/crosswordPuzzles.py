def find():
    global n, m, grid
    ans = '|'
    for y in range(n):
        word = []
        for x in range(m):
            if grid[y][x] == 'X':
                if len(word) > 1:
                    ans = min(ans, ''.join(word))
                word = []
            else:
                word.append(grid[y][x])
        if len(word) > 1:
            ans = min(ans, ''.join(word))
    return ans

for t in range(int(input())):
    n, m = map(int, input().split())
    grid = [list(input()) for _ in range(n)]
    ans = find()
    grid = list(zip(*grid))
    n, m = m, n
    ans = min(ans, find())
    print('Case {}: {}'.format(t+1, ans))