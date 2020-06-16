from math import ceil

for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    cnt = []
    cur = 0
    ans = 0
    for i, c in enumerate(s):
        if c == '0':
            cur += 1
        elif cur != 0:
            cnt.append(cur)
            cur = 0
    if cur != 0:
        cnt.append(cur)
    if s[0] == '0' and s[-1] == '0' and len(cnt) == 1:
        print(ceil(cnt[0] / (k+1)))
        continue
    if s[0] == '0':
        cnt[0] = max(0, cnt[0] - k)
        ans += ceil(cnt[0] / (k+1))
        cnt.pop(0)
    if s[-1] == '0':
        cnt[-1] = max(0, cnt[-1] - k)
        ans += ceil(cnt[-1] / (k+1))
        cnt.pop(-1)
    for c in cnt:
        ans += ceil(max(0, c - (k*2)) / (k+1))
    print(ans)