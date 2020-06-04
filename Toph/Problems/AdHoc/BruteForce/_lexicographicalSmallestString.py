from collections import Counter
n, k = map(int, input().split())
s = input()
cnt = Counter(s)
let = max([c for c in cnt.keys() if cnt[c] == k] or [-1])
if let == -1:
    print(s)
    exit(0)
ans = []
for c in s:
    if c == let and k > 1:
        k -= 1
    else:
        ans.append(c)
print(''.join(ans))