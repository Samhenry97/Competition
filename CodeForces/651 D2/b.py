for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    vis = [False] * (n*2)
    ans = []
    for i in range(n*2):
        for j in range(i+1, n*2):
            if not vis[j] and not vis[i] and l[i] % 2 == l[j] % 2:
                vis[i] = True
                vis[j] = True
                ans.append((i+1, j+1))
                break
    for i in range(n-1):
        print(*ans[i])