from math import sqrt
from math import acos
from math import sin
from math import pi

while True:
    try:
        r, x, y = map(float, input().split())
        d = sqrt(x**2 + y**2)
        if d >= r:
            print('miss')
            continue

        angle = 2 * acos(d / r)
        chordArea = (r**2 / 2) * (angle - sin(angle))
        otherArea = pi * r**2 - chordArea

        print(otherArea, chordArea)
        
    except EOFError:
        break
