s, n, m = map(int, input().split())
l1, l2 = [list(map(int, input().split())) for _ in range(2)]
max = -1
for y in l1:
    for x in l2:
        if y + x <= s and y + x > max:
            max = y + x
print(max)