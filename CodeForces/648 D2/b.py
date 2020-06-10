for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    v = list(map(int, input().split()))
    if len(set(v)) == 2:
        print('Yes')
    else:
        print(['No', 'Yes'][sorted(l) == l])