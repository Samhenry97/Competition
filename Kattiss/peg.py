grid = [[' ' for i in range(7)] for j in range(7)]

for y in range(7):
    s = input()
    for x in range(7):
        grid[y][x] = s[x]

ways = 0
for y in range(7):
    for x in range(7):
        if grid[y][x] == 'o':
            temp = y - 2 # Up
            if temp >= 0 and grid[temp + 1][x] == 'o' and grid[temp][x] == '.':
                ways += 1
                
            temp = x - 2 # Left
            if temp >= 0 and grid[y][temp + 1] == 'o' and grid[y][temp] == '.':
                ways += 1
                    
            temp = y + 2 # Down
            if temp < 7 and grid[temp - 1][x] == 'o' and grid[temp][x] == '.':
                ways += 1
                    
            temp = x + 2 # Right
            if temp < 7 and grid[y][temp - 1] == 'o' and grid[y][temp] == '.':
                ways += 1

print(ways)
