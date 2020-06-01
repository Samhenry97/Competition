l1, w1 = map(int, input().split())
l2, w2 = map(int, input().split())
l3, w3 = map(int, input().split())

r1 = (l1, w1)
r2 = (l2, w2)
r3 = (l3, w3)

remains = 0
width = 0
top = (0,0)
for i in (r1, r2, r3):
    if max(i) > width:
        top = i
        width = max(i)
        remains = max(i) - min(i)

found = False
others = []
for x in (r1, r2, r3):
    if found or x != top:
        others.append(x)
        found = True
x1 = others[0]
x2 = others[1]
if max(x1) == max(x2) == width:
    if (min(x1) + min(x2)) == remains:
        print(1)
    else:
        print(0)
    exit(0)

found = False
sum = 0
for i in x1:
    if found or i != remains:
        sum += i
    if i == remains:
        found = True
if not found:
    print(0)
    exit(0)

found = False
for i in x2:
    if found or i != remains:
        sum += i
    if i == remains:
        found = True
if not found:
    print(0)
    exit(0)
if sum == width:
    print(1)
else:
    print(0)
