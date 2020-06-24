input()
l = list(map(int, input().split()))
s = {}
for el in l:
    s[el] = s[el] + 1 if el in s else 1
count = 0
for k, v in s.items():
    count += v // 2
print(count)