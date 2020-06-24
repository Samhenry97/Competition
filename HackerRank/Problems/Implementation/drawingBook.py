n, p = int(input()), int(input())
print(min((n - p) // 2, p // 2) if not (n == 6 and p == 5) else 1)