for _ in range(int(input())):
    s = input()
    i = 1
    ans = 0
    while i < len(s):
        if s[i] != s[i-1]:
            ans += 1
            i += 1
        i += 1
    print(ans)
        