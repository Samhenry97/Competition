l = []
m = 0
for _ in range(int(input())):
    s = input()
    if len(s) % 2 != 1:
        if len(s) == 2:
            s = s + 'a'
        else:
            s = s[:-1]
    m = max(m, len(s))
    l.append(s)
for i in range(len(l)):
    print(' ' * ((m-len(l[i]))//2) + l[i])