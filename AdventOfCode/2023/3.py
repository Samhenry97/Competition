import math
from collections import defaultdict

with open('3.txt') as file:
   grid = file.read().split('\n')

deltas = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def part1():
  ans = 0
  digits = []
  valid = False
  for y, row in enumerate(grid):
    for x, c in enumerate(row + '.'):
      if not c.isdigit():
        if len(digits) > 0 and valid:
          ans += int(''.join(digits))
        digits = []
        valid = False
      elif c.isdigit():
        digits.append(c)
        for dy, dx in deltas:
          yy, xx = y + dy, x + dx
          if 0 <= yy < len(grid) and 0 <= xx < len(row):
            cc = grid[yy][xx]
            if cc != '.' and not cc.isdigit():
              valid = True
  return ans

def part2():
  asterisks = defaultdict(list)
  digits = []
  for y, row in enumerate(grid):
    for x, c in enumerate(row + '.'):
      if not c.isdigit():
        if len(digits) > 0:
          seen = set()
          num = int(''.join([d[0] for d in digits]))
          for _, y, x in digits:
            for dy, dx in deltas:
              yy, xx = y + dy, x + dx
              if (yy, xx) in seen:
                continue
              seen.add((yy, xx))
              if 0 <= yy < len(grid) and 0 <= xx < len(row):
                cc = grid[yy][xx]
                if cc == '*':
                  asterisks[(yy, xx)].append(num)
        digits = []
      if c.isdigit():
        digits.append((c, y, x))
  ans = 0
  for nums in asterisks.values():
    if len(nums) == 2:
      ans += math.prod(nums)
  return ans

# print(part1())
print(part2())
