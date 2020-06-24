input()
l = list(map(int, input().split()))
min = 999999999
for y in range(len(l)):
    for x in range(y + 1, len(l)):
        if l[y] == l[x] and x - y < min:
            min = x - y
print(min if min != 999999999 else -1)
            