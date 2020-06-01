for _ in range(int(input())):
    n = int(input())
    c = list(map(int, input().split()))
    a = 1
    sa = c[0]
    b = n-1
    sb = 0
    last = c[0]
    turn = False
    move = 1
    while a <= b:
        move += 1
        if turn:
            cur = 0
            while a <= b and cur <= last:
                sa += c[a]
                cur += c[a]
                a += 1
        else:
            cur = 0
            while a <= b and cur <= last:
                sb += c[b]
                cur += c[b]
                b -= 1
        last = cur
        turn = not turn
    print(move, sa, sb)