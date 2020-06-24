for _ in range(int(input())):
    n, c, m = map(int, input().split())
    choc = n // c
    wrap = choc
    free = 0

    while m <= wrap:
        give = wrap - wrap % m
        free = wrap // m
        wrap = wrap - give + free
        choc += free

    print(choc)
