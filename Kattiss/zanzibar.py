t = int(input())

for _ in range(t):
    l = list(map(int, input().split()))[:-1]
    last = l[0]
    totalImported = 0
    for i in range(1, len(l)):
        if last * 2 < l[i]:
            totalImported += l[i] - last * 2
        last = l[i]
    print(totalImported)
