while True:
    try:
        m, p, l, e, r, s, n = [int(x) for x in input().split()]

        nextM, nextP, nextL = 0, 0, 0
        for _ in range(n):
            nextM = p // s
            nextP = l // r
            nextL = m * e
            m, p, l = nextM, nextP, nextL

        print(m)
    except EOFError:
        break
