from math import sqrt

t = int(input())

for _ in range(t):
    s = input()

    grid = int(sqrt(len(s)))

    ans = []
    for x in range(grid - 1, -1, -1):
        for y in range(grid):
            ans.append(s[y * grid + x])
    print(''.join(ans))
            
