input()
a = list(map(int, input().split()))
if all([x == 0 for x in a]):
    print("NO")
else:
    print("YES")
    sec = []
    s = 0
    f = a[0] != 0
    for i, x in enumerate(a):
        if a[i] != 0:
            if f:
                if i > 0:
                    sec.append((s, i - 1))
                s = i
            else:
                f = True
    if s < len(a):
        sec.append((s, len(a) - 1))
    print(len(sec))
    for start, end in sec:
        print(start+1, end+1)

