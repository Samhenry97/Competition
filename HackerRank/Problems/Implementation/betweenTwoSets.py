n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
lower, upper = max(a), min(b) + 1
count = 0
for i in range(lower, upper):
    valid = True
    for el in a:
        if i % el != 0:
            valid = False
    for el in b:
        if el % i != 0:
            valid = False
    if valid:
        count += 1
print(count)