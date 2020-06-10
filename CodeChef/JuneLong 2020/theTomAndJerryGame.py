for _ in range(int(input())):
    t = int(input())
    while t % 2 == 0:
        t //= 2
    print(t // 2)