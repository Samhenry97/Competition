from math import sqrt, ceil

for _ in range(int(input())):
    n = int(input())
    while n % 2 == 0:
        n //= 2
    if n == 1:
        print(2)
        continue
    top = ceil(sqrt(n))
    ans = 0
    while True:
        found = False
        for i in range(3, top+1, 2):
            if n % i == 0:
                n //= i
                ans = max(ans, i)
                found = True
                break
        if not found:
            break
    print(ans if n == 1 else n)
