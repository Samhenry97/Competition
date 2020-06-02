a = [list(map(int, input().split())) for _ in range(2)]
b = [list(map(int, input().split())) for _ in range(2)]
c = [[0 for _ in range(2)] for _ in range(2)]
c[0][0] = a[0][0] * b[0][0] + a[0][1] * b[1][0]
c[0][1] = a[0][0] * b[0][1] + a[0][1] * b[1][1]
c[1][0] = a[1][0] * b[0][0] + a[1][1] * b[1][0]
c[1][1] = a[1][0] * b[0][1] + a[1][1] * b[1][1]
for i in range(2):
    print(*c[i])