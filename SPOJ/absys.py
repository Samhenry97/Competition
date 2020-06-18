for _ in range(int(input())):
    input()
    l, c = input().split(' = ')
    a, b = l.split(' + ')
    if 'machula' in c:
        print('{} + {} = {}'.format(a, b, int(a) + int(b)))
    elif 'machula' in a:
        print('{} + {} = {}'.format(int(c) - int(b), b, c))
    else:
        print('{} + {} = {}'.format(a, int(c) - int(a), c))
        