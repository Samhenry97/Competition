input()
l = list(map(int, input().split()))

l.sort()
max = 1
for i, el in enumerate(l):
    tmp = i
    while tmp < len(l) and l[tmp] - el <= 1:
        tmp += 1
    if tmp - i > max:
        max = tmp - i
print(max)