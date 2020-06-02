h, t = map(int, input().split())
while t > 0:
    if t > 1:
        print('TT')
        t -= 2
        h += 1
    else:
        print('T')
        print('TT')
        t = 0
        h += 1
if h % 2 == 0:
    print('\n'.join(['HH'] * (h//2)))
else:
    h += 1
    print('H')
    print('\n'.join(['T'] * 3))
    print('\n'.join(['TT'] * 2))
    print('\n'.join(['HH'] * (h//2)))

