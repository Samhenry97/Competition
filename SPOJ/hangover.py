n = float(input())
while n:
    cur = 0.0
    for i in range(2, 100000):
        if cur + 1 / i > n:
            print('{} card(s)'.format(i-1))
            break
        cur += 1 / i
    n = float(input())