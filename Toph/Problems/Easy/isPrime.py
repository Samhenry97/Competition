from math import floor, sqrt
n = int(input())
for i in range(2, floor(sqrt(n))):
    if n % i == 0:
        print('No')
        exit(0)
print('Yes')
