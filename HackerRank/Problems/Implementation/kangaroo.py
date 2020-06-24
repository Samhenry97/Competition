x1, v1, x2, v2 = map(int, input().split())
if x1 > x2:
    x1, x2 = x2, x1
    v1, v2 = v2, v1
if v2 >= v1:
    print('NO')
    exit(0)
while x1 < x2:
    x1 += v1
    x2 += v2
print('YES' if x1 == x2 else 'NO')