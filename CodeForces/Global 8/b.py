n = int(input())
cnt = 1
while cnt ** 10 < n:
    cnt += 1
for i in range(10):
    tmp = 1
    for j in range(10):
        if j <= i:
            tmp *= cnt
        else:
            tmp *= cnt-1
    if tmp >= n:
        for j, c in enumerate('codeforces'):
            print(c * cnt if j <= i else c * (cnt-1), end='')
        print()
        exit(0)
