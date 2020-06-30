for _ in range(int(input())):
    s = input()
    low = 0
    cur = 0
    ans = 0
    for i, c in enumerate(s):
        ans += 1
        cur += 1 if c == '+' else -1
        if cur < low:
            low = cur
            ans += i + 1
    print(ans)