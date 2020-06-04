for t in range(int(input())):
    n, c, b = int(input()), int(input()), int(input())
    l = list(map(int, input().split()))
    ans = 0
    if c == 1:
        ans = l.count(b)
    elif c == 2:
        for i in range(n):
            for j in range(i+1, n):
                if l[i] + l[j] == b:
                    ans += 1
    else:
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if l[i] + l[j] + l[k] == b:
                        ans += 1
    print('Case {}: {}'.format(t+1, ans))