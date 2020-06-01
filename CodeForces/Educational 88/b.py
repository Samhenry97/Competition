for _ in range(int(input())):
    n, m, one, two = map(int, input().split())
    grid = [input() for _ in range(n)]
    usey = two <= one * 2
    ans = 0
    for y in range(n):
        cnt = 0
        for x in range(m):
            if grid[y][x] == '.':
                cnt += 1
                if usey:
                    if cnt == 2:
                        ans += two
                        cnt = 0
                else:
                    ans += one
            else:
                if usey:
                    if cnt == 2:
                        ans += two
                    elif cnt == 1:
                        ans += one
                    cnt = 0
        if usey:
            if cnt == 2:
                ans += two
            elif cnt == 1:
                ans += one
    print(ans)