n, k = map(int, input().split())
mod = [0] * k
for el in list(map(int, input().split())):
    mod[el % k] += 1
count = min(mod[0], 1)
for i in range(1, k//2+1):
    if i != k - i:
        count += max(mod[i], mod[-i])
if not (k & 1):
    count += 1
print(count)