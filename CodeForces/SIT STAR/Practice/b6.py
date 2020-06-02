from math import floor

a, b = map(int, input().split())
while a != b:
    if a > b:
        a = floor(a/2)
    elif b > a:
        b = floor(b/2)
print(a)
