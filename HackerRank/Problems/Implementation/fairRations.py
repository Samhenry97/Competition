n = int(input())
l = list(map(int, input().split()))
ans = 0
for i in range(len(l)-1):
    if l[i] % 2 == 1:
        l[i] += 1
        l[i+1] += 1
        ans += 2
print('NO' if l[-1] % 2 == 1 else ans)