def myint(s):
    if s.strip(): return int(s)
    else: return 0

found = False
for i in range(int(input()), int(input()) + 1):
    l = len(str(i))
    n = str(i ** 2)
    if myint(n[:-l]) + myint(n[-l:]) == int(i):
        print(i, end=' ')
        found = True
print('' if found else 'INVALID RANGE')