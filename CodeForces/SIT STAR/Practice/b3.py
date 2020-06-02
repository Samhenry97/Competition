x, y, z, m = map(int, input().split())
p = sorted([x, y, z])
cur = 0
cnt = 0
ans = 1
while cur < len(p):
    cnt += p[cur]
    if cnt > m:
        ans += 1
        cur -= 1
        cnt = 0
    cur += 1
print(ans)