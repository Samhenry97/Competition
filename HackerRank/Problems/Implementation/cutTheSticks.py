total = int(input())
l = list(map(int, input().split()))
while total:
    print(total)
    sub = min([x for x in l if x > 0])
    for i in range(len(l)):
        if l[i] > 0:
            l[i] -= sub
            if l[i] <= 0:
                total -= 1