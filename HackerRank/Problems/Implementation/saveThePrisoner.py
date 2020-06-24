for _ in range(int(input())):
    n, m, s = map(int, input().split())
    print(n if (s + m - 1) % n == 0 else (s + m - 1) % n)