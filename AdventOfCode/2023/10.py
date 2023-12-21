from collections import deque

with open('10.txt') as file:
  grid = [list(s) for s in file.read().split('\n')]

def part1():
  deltas = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}
  pipes = {'|': {'N', 'S'}, '-': {'E', 'W'}, 'L': {'N', 'E'}, 'J': {'N', 'W'}, '7': {'S', 'W'}, 'F': {'S', 'E'}, '.': {}}
  opposites = {'N': 'S', 'S': 'N', 'W': 'E', 'E': 'W'}

  queue = deque()
  for y in range(len(grid)):
    if 'S' in grid[y]:
      x = grid[y].index('S')
      for dir, (dy, dx) in deltas.items():
        yy, xx = y + dy, x + dx
        pipe = grid[yy][xx]
        if opposites[dir] in pipes[pipe]:
          queue.append((yy, xx, next(iter(pipes[pipe] - {opposites[dir]})), 1))
          grid[yy][xx] = '.'
  
  ans = 0
  while len(queue) > 0:
    y, x, dir, steps = queue.popleft()
    ans = max(steps, ans)
    yy, xx = y + deltas[dir][0], x + deltas[dir][1]
    pipe = grid[yy][xx]
    if pipe != '.':
      queue.append((yy, xx, next(iter(pipes[pipe] - {opposites[dir]})), steps + 1))
      grid[yy][xx] = '.'
  return ans

def part2():
  pass

print(part1())
# print(part2())
