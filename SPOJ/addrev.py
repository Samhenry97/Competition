for _ in range(int(input())):
    a, b = [x[::-1] for x in input().split()]
    print(int(str(int(a) + int(b))[::-1])) 