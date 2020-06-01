from math import pi

while True:
    D, V = map(float, input().split())
    if D == 0 and V == 0:
        break
    
    r = D / 2
    num = 6 * (-V - (2/3)*pi*r**3 + pi*r**2*D)
    goal = pow(num / pi, 1/3)
    
    print(goal)

