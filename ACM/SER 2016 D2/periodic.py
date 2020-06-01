s = input()
l = len(s)
for k in range(1, l // 2 + 2):
    if l % k != 0:
        continue
    sub = s[:k]
    tmp = ""
    next = sub
    for j in range(l//k):
        tmp += next
        next = next[-1] + next[:-1]
    if s == tmp:
        print(k)
        exit(0)
print(len(s))
