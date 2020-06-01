n, p = map(int, input().split())

data = []
for _ in range(n):
    data.append(float(input()))

avg = sum(data) / len(data)
avg *= .8

indices = {x:1 for x in range(len(data)) if data[x] < avg}


while p <= n:
    for i in range(p):
        if i in indices:
            works = True
            for k in range(i, n, p):
                if k not in indices:
                    works = False
            if works:
                print(p)
                exit(0)
    p += 1
print(-1)
