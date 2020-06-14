for _ in range(int(input())):
    n, x, m = map(int, input().split())
    al, ar = x, x
    for _ in range(m):
        l, r = map(int, input().split())
        if l <= ar and al <= r:
            al = min(al, l)
            ar = max(ar, r)
    print(ar - al + 1)