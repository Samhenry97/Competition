input()
l = list(map(int, input().split()))
mincount = 0
maxcount = 0
min = l[0]
max = l[0]
for el in l:
    if el > max:
        max = el
        maxcount += 1
    if el < min:
        min = el
        mincount += 1
print(maxcount, mincount)