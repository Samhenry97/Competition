n = int(input())

while n != 0:
    l = []
    s = []
    for _ in range(n):
        l.append(int(input()))
    s = sorted(l)

    final = []
    for _ in range(n):
        final.append(int(input()))
    final.sort()
    for x in l:
        print(final[s.index(x)])
    print()
    n = int(input())
