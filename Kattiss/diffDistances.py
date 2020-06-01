l = list(map(float, input().split()))

while len(l) > 1:
    ans = (abs(l[0] - l[2]) ** l[4] + abs(l[1] - l[3]) ** l[4]) ** (1 / l[4])
    print(ans)
    l = list(map(float, input().split()))
