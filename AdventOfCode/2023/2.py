import math

with open('2.txt') as file:
  data = file.read().split('\n')

def part1():
  ans = 0
  cubes = {'red': 12, 'green': 13, 'blue': 14}
  for i, game in enumerate(data):
    legal = True
    moves = game.split(':')[1].split(';')
    for move in moves:
      grabs = [grab.strip().split() for grab in move.split(',')]
      for num, color in grabs:
        if cubes[color] < int(num):
          legal = False
    if legal:
      ans += i + 1
  return ans

def part2():
  ans = 0
  for game in data:
    mins = {'red': 0, 'green': 0, 'blue': 0}
    moves = game.split(':')[1].split(';')
    for move in moves:
      grabs = [grab.strip().split() for grab in move.split(',')]
      for num, color in grabs:
        mins[color] = max(mins[color], int(num))
    ans += math.prod(mins.values())
  return ans

# print(part1())
print(part2())
