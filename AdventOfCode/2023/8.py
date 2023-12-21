import re
import math

with open('8.txt') as file:
  data = file.read().split('\n')

def part1():
  sequence = data[0]
  graph = {}
  for node in data[2:]:
    match = re.search(r"([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)", node)
    id, l, r = match.groups()
    graph[id] = {'L': l, 'R': r}
  
  current = 'AAA'
  steps = 0
  index = 0
  while current != 'ZZZ':
    current = graph[current][sequence[index]]
    steps += 1
    index = (index + 1) % len(sequence)
  return steps

def part2():
  sequence = data[0]
  graph = {}
  for node in data[2:]:
    match = re.search(r"([0-9A-Z]{3}) = \(([0-9A-Z]{3}), ([0-9A-Z]{3})\)", node)
    id, l, r = match.groups()
    graph[id] = {'L': l, 'R': r}
  
  current = [id for id in graph.keys() if id[-1] == 'A']
  lengths = []
  for id in current:
    steps = 0
    index = 0
    while id[-1] != 'Z':
      id = graph[id][sequence[index]]
      steps += 1
      index = (index + 1) % len(sequence)
    lengths.append(steps)
  return math.lcm(*lengths)

# print(part1())
print(part2())