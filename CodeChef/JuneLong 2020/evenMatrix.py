for _ in range(int(input())):
    n = int(input())
    for i in range(n):
        if n % 2 == 1 or i % 2 == 0:
            print(*list(range(n * i + 1, n * i + n + 1)))
        else:
            print(*list(range(n * i + n, n * i, -1)))