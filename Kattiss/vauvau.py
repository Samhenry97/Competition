a, b, c, d = map(int, input().split())
p, m, g = map(int, input().split())
p -= 1
m -= 1
g -= 1

dog1 = sum([a, b])
dog2 = sum([c, d])

rP = (p % dog1 < a) + (p % dog2 < c)
rM = (m % dog1 < a) + (m % dog2 < c)
rG = (g % dog1 < a) + (g % dog2 < c)

ans = { 0: 'none', 1: 'one', 2: 'both' }

print(ans[rP])
print(ans[rM])
print(ans[rG])
