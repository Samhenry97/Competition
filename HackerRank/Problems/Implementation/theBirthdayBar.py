input()
l = list(map(int, input().split()))
d, m = map(int, input().split())
count = 0
for y in range(0, len(l) - m + 1):
    if sum(l[y:y+m]) == d:
        count += 1
print(count)
        