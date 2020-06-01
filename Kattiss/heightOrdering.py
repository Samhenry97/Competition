t = int(input())

oo = 1 << 31

for _ in range(t):
    l = list(map(int, input().split()))
    step = l[0]
    l = l[1::]

    total = 0
    cursor = 0
    m = min(l)
    while(m != oo):
        total += l.index(m) - cursor
        l.remove(m)
        l.insert(cursor, oo)
        cursor += 1
        
        m = min(l)
    print(step, total)
        
