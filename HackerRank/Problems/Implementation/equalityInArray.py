input()
l = list(map(int, input().split()))
c = {}
for el in l:
    c[el] = c[el] + 1 if el in c else 1
print(len(l) - max(c.values()))