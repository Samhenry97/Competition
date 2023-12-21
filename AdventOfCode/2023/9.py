with open('9.txt') as file:
  data = file.read().split('\n')

def part1():
  ans = 0
  for line in data:
    grid = [[int(x) for x in line.split()]]
    while not all([x == 0 for x in grid[-1]]):
      grid.append([grid[-1][i] - grid[-1][i-1] for i in range(1, len(grid[-1]))])
    for i in range(len(grid)-1, 0, -1):
      grid[i-1].append(grid[i-1][-1] + grid[i][-1])
    ans += grid[0][-1]
  return ans

def part2():
  ans = 0
  for line in data:
    grid = [[int(x) for x in line.split()]]
    while not all([x == 0 for x in grid[-1]]):
      grid.append([grid[-1][i] - grid[-1][i-1] for i in range(1, len(grid[-1]))])
    for i in range(len(grid)-1, 0, -1):
      grid[i-1].insert(0, grid[i-1][0] - grid[i][0])
    ans += grid[0][0]
  return ans

# print(part1())
print(part2())
