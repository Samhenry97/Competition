t = int(input())
c = 3
while c < t:
    t -= c
    c *= 2
print(c - t + 1)