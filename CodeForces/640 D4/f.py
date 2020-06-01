for _ in range(int(input())):
    n0, n1, n2 = map(int, input().split())
    s = ''
    if n0 > 0 and n2 > 0:
        if n1 % 2 == 0:
            n1 -= 1
            s = '1'
        alt = ''.join(['0' if i % 2 == 0 else '1' for i in range(n1)])
        s += '0' * n0 + alt + '1' * (n2+1)
    elif n0 > 0:
        s = '0' * (n0+1)
        s += ''.join(['1' if i % 2 == 0 else '0' for i in range(n1)])
    elif n2 > 0:
        s = '1' * (n2+1)
        s += ''.join(['0' if i % 2 == 0 else '1' for i in range(n1)])
    else:
        s = '1'
        s += ''.join(['0' if i % 2 == 0 else '1' for i in range(n1)])
    print(s)