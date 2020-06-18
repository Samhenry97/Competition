for _ in range(int(input())):
    input()
    s = input()[:-2].split()
    while len(s) > 1:
        ans = int(eval(s[0] + s[1] + s[2]))
        s = s[2:]
        s[0] = str(ans)
    print(s[0]) 