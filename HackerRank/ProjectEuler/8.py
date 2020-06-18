from functools import reduce

for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    ans = 0
    for i in range(n-k):
        ans = max(ans, reduce(lambda x, y: x * y, [int(c) for c in s[i:i+k]]))
    print(ans)