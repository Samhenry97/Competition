for _ in range(int(input())):
    n = int(input())
    s = set(map(int, input().split()))
    found = False
    for i in range(1, 1024):
        ns = set([c ^ i for c in s])
        if s == ns:
            print(i)
            found = True
            break
    if not found:
        print(-1)
    