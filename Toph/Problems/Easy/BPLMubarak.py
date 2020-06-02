for _ in range(int(input())):
    s = input()
    cnt = len([c for c in s if c.isnumeric() or c == 'O'])
    o = cnt // 6
    b = cnt % 6
    over = '{} OVER{}'.format(o, 'S' if o > 1 else '')
    ball = '{} BALL{}'.format(b, 'S' if b > 1 else '')
    if o:
        print(over, end='')
    if o and b:
        print(' ', end='')
    if b:
        print(ball, end='')
    print()
