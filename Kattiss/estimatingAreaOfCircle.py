from math import pi

while True:
    r, m, c = map(float, input().split())

    if r == 0 and m == 0 and c == 0:
        break
    
    trueArea = pi * r ** 2
    estimate = r ** 2 * 4 * (c / m)
    print(trueArea, estimate)
