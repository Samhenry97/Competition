s = input()

t = 0
c = 0
g = 0
for ch in s:
    if ch == 'T':
        t += 1
    elif ch == 'C':
        c += 1
    elif ch == 'G':
        g += 1

add = min(t, g, c) * 7
print(t ** 2 + c ** 2 + g ** 2 + add)
