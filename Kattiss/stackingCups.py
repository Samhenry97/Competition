items = int(input())

l = []
for _ in range(items):
    s = input().split()
    try:
        r = int(s[0])
        l.append((r, s[1]))
    except:
        l.append((int(s[1]) * 2, s[0]))

l.sort()
for item in l:
    print(item[1])
