for _ in range(int(input())):
    n = int(input())
    p = -1
    for a in range(n//3):
        b = (n**2 - 2*n*a) // (2*n - 2*a)
        c = n - a - b
        if c**2 == a**2 + b**2:
            tmp = a*b*c
            if tmp and tmp > p:
                p = tmp
    print(p)
