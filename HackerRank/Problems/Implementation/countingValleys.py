input()
s = input()
lastDist = 0
dist = 0
count = 0
for c in s:
    if c == 'U':
        dist += 1
    else:
        dist -= 1
    if dist == 0:
        if lastDist == -1:
            count += 1
    lastDist = dist
print(count)