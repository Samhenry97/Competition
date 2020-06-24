n, m = map(int, input().split())
peeps = []
for _ in range(n):
    peeps.append(int(input(), 2))
    
big = 0
team = 0
for y in range(n):
    for x in range(y + 1, n):
        test = bin(peeps[y] | peeps[x]).count('1')
        if test > big:
            big = test
            team = 1
        elif test == big:
            team += 1
print(big)
print(team)