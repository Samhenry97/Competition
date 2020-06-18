ss = [1]
sn = [1]
for i in range(2, 10001):
    ss.append(ss[-1] + i**2)
    sn.append(sn[-1] + i)

for _ in range(int(input())):
    n = int(input())
    print(sn[n-1]**2 - ss[n-1])