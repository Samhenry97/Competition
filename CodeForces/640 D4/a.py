for _ in range(int(input())):
    n = input()
    ans = [c for c in n if c != '0']
    print(len(ans))
    for i in range(len(n)):
        c = n[len(n)-i-1]
        if c != '0':
            print(c + '0' * i, end=' ')
    print()