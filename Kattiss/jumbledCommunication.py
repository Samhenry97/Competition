input()

final = []
bArray = list(map(int, input().split()))
for b in bArray:
    for i in range(100000):
        test = i ^ (i << 1)
        if b == test:
            final.append(str(i))
            break

print(' '.join(final))
