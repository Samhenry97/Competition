for _ in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    l1 = [a[i//2] if i % 2 == 0 else b[i//2] for i in range(n*2)]
    l2 = [b[i//2] if i % 2 == 0 else a[i//2] for i in range(n*2)]
    print(['NO', 'YES'][sorted(l1) == l1 or sorted(l2) == l2])