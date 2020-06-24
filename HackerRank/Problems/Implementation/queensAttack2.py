n, k = map(int, input().split())
y, x = map(int, input().split())
left = x - 1
right = n - x
up = n - y
down = y - 1
upright = n - max(y, x)
downright = min(n - x, y - 1)
upleft = min(n - y, abs(1 - x))
downleft = min(y, x) - 1
for _ in range(k):
    yo, xo = map(int, input().split())
    if xo == x and yo > y and yo - y < up:
        up = yo - y - 1
    elif xo == x and yo < y and y - yo < down:
        down = y - yo - 1
    elif yo == y and xo < x and x - xo < left:
        left = x - xo - 1
    elif yo == y and xo > x and xo - x < right:
        right = xo - x - 1
    elif yo > y and xo > x and yo - y == xo - x and yo - y < upright:
        upright = yo - y - 1
    elif yo < y and xo < x and y - yo == x - xo and y - yo < downleft:
        downleft = y - yo - 1
    elif yo < y and xo > x and y - yo == xo - x and y - yo < downright:
        downright = y - yo - 1
    elif yo > y and xo < x and yo - y == x - xo and yo - y < upleft:
        upleft = yo - y - 1
print(left + right + up + down + upright + downright + upleft + downleft)
