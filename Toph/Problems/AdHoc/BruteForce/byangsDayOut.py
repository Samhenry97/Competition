for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print(['No', 'Yes'][all([a+b>=c, b+c>=a, a+c>=b])])