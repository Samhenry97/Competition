n, k = map(int, input().split())
l = list(map(int, input().split()))
count = 0
for y in range(len(l)):
    for x in range(y + 1, len(l)):
        if (l[y] + l[x]) % k == 0:
            count += 1
print(count)