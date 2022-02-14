import math
 
for _ in range(int(input())):
    n, k = map(int, input().split())
    h = 0
    cur = 1
    batch = 1
    while cur < n and batch != k:
        cur += batch
        h += 1
        batch = min((batch * 2), k)
    if cur < n:
        h += (n - cur) // batch
        if (n - cur) % batch > 0:
            h += 1
    print(h)
