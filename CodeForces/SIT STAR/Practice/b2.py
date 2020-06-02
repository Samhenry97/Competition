n, m = map(int, input().split())
print(['Yes', 'No'][n % 2 == 1 and m % 2 == 1])