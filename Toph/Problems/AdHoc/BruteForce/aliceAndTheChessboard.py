for _ in range(int(input())):
    x, y, tx, ty = map(int, input().split())
    print(['No', 'Yes'][abs(tx-x) == abs(ty-y)])