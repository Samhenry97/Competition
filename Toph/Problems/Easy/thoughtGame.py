for _ in range(int(input())):
    x, y = map(int, input().split())
    print(['Oops!', 'Sadia will be happy.'][(x+y)//2 % 2 == 0])