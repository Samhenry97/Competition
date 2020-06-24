n, m = map(int, input().split())
l = sorted(list(map(int, input().split())))
s = l[0]
ans = l[0]
for i in range(1, len(l)):
    d = l[i] - s
    s = l[i]
    ans = max(ans, d // 2)
ans = max(ans, n-1 - l[-1])
print(ans)