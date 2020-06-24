for _ in range(int(input())):
    n, a, b = int(input()) - 1, int(input()), int(input())
    a, b = sorted([a, b])
    d = b - a
    cur, end = a * n, b * n
    if a == b:
        print(cur, end=' ')
    else:
        while cur <= end:
            print(cur, end=' ')
            cur += d
    print()