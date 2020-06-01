r1 = list(map(int, input().split()))
r2 = list(map(int, input().split()))
r3 = list(map(int, input().split()))

l = [r1[0], r1[1], r2[0], r2[1], r3[0], r3[1]]
width = max(l)
if l.count(width) == 3:
    if sum([x for x in l if x != width]) == width:
        print(1)
    else:
        print(0)
    exit(0)
elif l.count(width) == 2:
    print(0)
    exit(0)

if width in r1:
    remains = width - min(r1)
    if remains in r2 and remains in r3:
        r2.remove(remains)
        r3.remove(remains)
        print(1) if r2[0] + r3[0] == width else print(0)
        exit(0)
    else:
        print(0)
        exit(0)
elif width in r2:
    remains = width - min(r2)
    if remains in r1 and remains in r3:
        r1.remove(remains)
        r3.remove(remains)
        print(1) if r1[0] + r3[0] == width else print(0)
        exit(0)
    else:
        print(0)
        exit(0)
else:
    remains = width - min(r3)
    if remains in r1 and remains in r2:
        r1.remove(remains)
        r2.remove(remains)
        print(1) if r1[0] + r2[0] == width else print(0)
        exit(0)
    else:
        print(0)
        exit(0)
