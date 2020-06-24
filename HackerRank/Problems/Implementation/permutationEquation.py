n = int(input())
l = [0] * (n + 1)
data = list(map(int, input().split()))
idx = 0
for i in range(1, n + 1):
    l[data[idx]] = i
    idx += 1
for i in range(1, n + 1):
    print(l[l[i]])