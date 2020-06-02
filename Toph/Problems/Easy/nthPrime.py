from math import ceil, sqrt
MAXN = 10000000
n = int(input())
a = [True] * MAXN
cnt = 0
for p in range(2, MAXN):
    if a[p]:
        cnt += 1
        if cnt == n:
            print(p)
            exit(0)
        for i in range(p*p, MAXN, p):
            a[i] = False