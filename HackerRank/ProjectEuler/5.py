from math import gcd

ans = [1]
for i in range(2, 41):
    ans.append(ans[-1] * i // gcd(ans[-1], i))

for _ in range(int(input())):
    print(ans[int(input())-1])
