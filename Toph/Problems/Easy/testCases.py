n, cpul, meml = map(int, input().split())
for _ in range(n):
    d, c, m = map(int, input().split())
    if c > cpul:
        print('CLE')
        exit(0)
    elif m > meml:
        print('MLE')
        exit(0)
    elif d != 0:
        print('WA')
        exit(0)
print('AC')