from functools import cmp_to_key

map = {}

def cmp(a, b, flag=False):
    if b in map[a]:
        return 1
    for x in map[a]:
        if cmp(x, b) == 1:
            #print("return 1")
            return 1
    if a in map[b]:
        return -1
    for x in map[b]:
        if cmp(a, x) == -1:
            return -1
    if flag:
        return 0
    return 10/0

lets, n = input().split()
n = int(n)

letters = 'abcdefghijklmnopqrstuvwxyz'[:ord(lets) - ord('a') + 1]

c = 'a'
while c <= lets:
    map[c] = []
    c = chr(ord(c) + 1)

last = input()
l = [list(last)]
for i in range(n - 1):
    cur = input()
    l.append(list(cur))
    for a, b in zip(last, cur):
        if a != b:
            map[a].append(b)
            if cmp(a, b, True) == cmp(b, a, True) != 0:
                print(1)
                exit(0)
            break
    last = cur

flag2 = False
try:
    final = sorted(letters, key=cmp_to_key(cmp))

    l2 = []
    s = ''.join(final)[::-1]
    for st in l:
        for i in range(len(st)):
            st[i] = letters[s.index(st[i])]
        l2.append(''.join(st))
    for s1, s2 in zip(sorted(l2), l):
        if s1 != ''.join(s2):
            print(1)
            flag2 = True
            exit(0)

    print(s)
except:
    if not flag2:
        print(0)
    exit(0)
