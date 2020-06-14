for _ in range(int(input())):
    a, b = map(int, input().split())
    ans = 0
    while a != b and a > 0 and b > 0:
        a, b = max(a, b), min(a, b)
        diff = max(1, min((a - b) // 2, b))
        a -= diff * 2
        b -= diff
        ans += diff
    if a == b:
        ans += (a // 3) * 2
        a %= 3
        if a == 2:
            ans += 1
    print(ans)