for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if abs(c - b) < abs(c - a):
        print('Cat B')
    elif abs(c - b) > abs(c - a):
        print('Cat A')
    else:
        print('Mouse C')