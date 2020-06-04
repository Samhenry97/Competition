from math import sqrt
def dist(p1, p2):
    return (p1[0]-p2[0])**2+(p1[1]-p2[1])**2

for t in range(int(input())):
    n = int(input())
    ans = 0
    c = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            ans = max(ans, dist(c[i], c[j]))
    print('Case {}: {}'.format(t+1, ans))