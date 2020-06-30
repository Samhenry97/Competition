for _ in range(int(input())):
    l = list(input())
    ans = True
    while len(l) >= 2:
        found = False
        for i in range(1, len(l)):
            if l[i] != l[i-1]:
                ans = not ans
                del l[i]
                del l[i-1]
                found = True
                break
        if not found:
            break
    print(['DA', 'NET'][ans])
        