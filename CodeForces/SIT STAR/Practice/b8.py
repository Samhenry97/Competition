from collections import defaultdict
s = input()
n, mid = len(s), len(s)//2
s1 = sorted([c for i, c in enumerate(s) if i % 2 == 0])
s2 = sorted([c for i, c in enumerate(s) if i % 2 == 1])

if n == 1:
    print(s)
    exit(0)

ans = [None] * len(s)
if len(s) % 2 == 0:
    for i in range(mid):
        if s1[i] != s2[i]:
            print('NO')
            exit(0)
        ans[i*2] = s1[i]
        ans[-i*2-1] = s2[i]
    print(''.join(ans))
else:
    tmp = s1 if len(s1) % 2 == 1 else s2
    cnt = defaultdict(int)
    for c in tmp:
        cnt[c] += 1
    for k, v in cnt.items():
        if v % 2 == 1:
            i = tmp.index(k)
            ans[mid] = tmp[i]
            tmp.pop(i)
            break
    for i in range(len(s1)//2):
        if s1[i*2] != s1[i*2+1]:
            print('NO')
            exit(0)
        ans[i*2] = s1[i*2]
        ans[-i*2-1] = s1[i*2+1]
    for i in range(len(s2)//2):
        if s2[i*2] != s2[i*2+1]:
            print('NO')
            exit(0)
        ans[i*2+1] = s2[i*2]
        ans[-i*2-2] = s2[i*2+1]
    print(''.join(ans))