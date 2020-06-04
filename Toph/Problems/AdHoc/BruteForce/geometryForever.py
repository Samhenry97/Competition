a, b = map(int, input().split())
ans = 0
for c in range(1, a+b):
    ans += (a+b>c and a+c>b and b+c>a)
print(ans)