n, d = map(int, input().split())
l, c = list(map(int, input().split())), 0

for i in range(n):
    if l[i] + d in l and l[i] + 2 * d in l: c += 1
print(c)