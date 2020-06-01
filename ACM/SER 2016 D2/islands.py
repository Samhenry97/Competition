def equals(x, y):
    if x == y:
        return True
    if x == 'C' and y == 'L':
        return True
    if x == 'L' and y == 'C':
        return True
    return False

r, c1 = map(int, input().split())
map = []
l = []
def root(x1):
    while str(l[x1]).isnumeric():
        x1 = l[x1]
    return x1

for x in range(r):
  s = input()
  i = -1
  for c in s:
    if i >= 0 and x > 0 and c in ('C', 'L') and s[i] in ('C', 'L') and map[x - 1][i + 1] in ('C', 'L') and root(x * c1 + i) != root((x - 1) * c1 + i + 1):
        l[root(x * c1 + i)] = root((x - 1) * c1 + i + 1)
        l.append(root((x - 1) * c1 + i + 1))
        if c == 'L' or s[i] == 'L' or map[x - 1][i + 1] == 'L':
            l[root((x - 1) * c1 + i + 1)] = 'L'
    elif i >= 0 and c in ('C', 'L') and s[i] in ('C', 'L'):
        #print("Choice 1")
        l.append(root(x * c1 + i))
        if c == 'L' or s[i] == 'L':
            l[root(x * c1 + i)] = 'L'
    elif x > 0 and c in ('C', 'L') and map[x - 1][i + 1] in ('C', 'L'):
        #print("Choice 2")
        l.append(root((x - 1) * c1 + i + 1))
        if c == 'L' or map[x - 1][i + 1] == 'L':
            l[root((x - 1) * c1 + i + 1)] = 'L'
    else:
        #print("Choice 3")
        l.append(c)
    i += 1
  map.append(s)
  #print()
print(len([x for x in l if x == 'L']))
