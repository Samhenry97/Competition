for _ in range(int(input())):
    a, b = map(int, input().split())
    a, b = max(a, b), min(a, b)
    if a == b:
        print(0)
        continue
    sa = list(bin(a)[2:])
    sb = list(bin(b)[2:])
    cnt = 0
    while sa != sb and len(sa) > 0 and sa[-1] != '1':
        sa.pop()
        cnt += 1
    if sa == sb:
        ans = 0
        while cnt >= 3:
            cnt -= 3
            ans += 1
        while cnt >= 2:
            cnt -= 2
            ans += 1
        ans += cnt
        print(ans)
    else:
        print(-1)