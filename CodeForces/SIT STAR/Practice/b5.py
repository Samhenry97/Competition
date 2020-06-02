from math import sqrt, floor
b, w = map(int, input().split())
if b == w:
    print(floor(sqrt(b * 2)))
else:
    print(floor(sqrt(min(b, w) * 2 + 1)))