s = input()
d = int(input())
cov = d
z = 0
ans = 0
for c in s:
    if c == '0':
        z += 1
        cov -= 1
        if cov == 0:
            ans += 1
            cov = d
    else:
        cov = d
        z = 0
print(ans)
