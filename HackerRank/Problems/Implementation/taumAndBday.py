for _ in range(int(input())):
    b, w = map(int, input().split())
    x, y, z = map(int, input().split())
    if z >= abs(x - y):
        print(b * x + w * y)
    elif x <= y:
        print((b + w) * x + w * z)
    else:
        print((b + w) * y + b * z)