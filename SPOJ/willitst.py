n = int(input())
f = set()
while n not in f and n > 1:
    f.add(n)
    n = n // 2 if n % 2 == 0 else 3 * n + 3
print(['NIE', 'TAK'][n == 1])