import math
from collections import defaultdict, deque

with open('5.txt') as file:
  data = file.read().split('\n')

def part1():
  seeds = []
  ranges = defaultdict(list)
  graph = dict()
  metric = None

  for line in data:
    if line.startswith('seeds:'):
      seeds = [int(seed) for seed in line.split()[1:]]
    elif line.endswith('map:'):
      source, _, destination = line.split()[0].split('-')
      graph[source] = destination
      metric = source
    elif len(line) > 0:
      dest, source, dist = [int(x) for x in line.split()]
      ranges[metric].append((dest, source, dist))
  
  # Convert one seed at a time and check the result
  ans = math.inf
  for seed in seeds:
    metric = 'seed'
    value = seed
    while metric != 'location':
      for dest, source, dist in ranges[metric]:
        if source <= value <= source + dist - 1:
          value = dest - source + value
          break
      metric = graph[metric]
    ans = min(value, ans)
  return ans

def part2():
  def segment_sieve(flour, sieve):
    nonoverlap = []
    if flour[0] < sieve[0]:
      # Left side non-overlap
      nonoverlap.append((flour[0], min(flour[1], sieve[0] - 1)))
    if flour[1] > sieve[1]:
      # Right side non-overlap
      nonoverlap.append((max(flour[0], sieve[1] + 1), flour[1]))

    if flour[0] <= sieve[1] and sieve[0] <= flour[1]:
      # Overlap exists!
      return (max(flour[0], sieve[0]), min(flour[1], sieve[1])), nonoverlap
    else:
      return None, nonoverlap

  seeds = deque()
  ranges = defaultdict(list)
  graph = dict()
  metric = None

  for line in data:
    if line.startswith('seeds:'):
      seed_data = [int(seed) for seed in line.split()[1:]]
      for i in range(0, len(seed_data), 2):
        seeds.append((seed_data[i], seed_data[i] + seed_data[i + 1] - 1))
    elif line.endswith('map:'):
      source, _, destination = line.split()[0].split('-')
      graph[source] = destination
      metric = source
    elif len(line) > 0:
      dest, source, dist = [int(x) for x in line.split()]
      ranges[metric].append((dest, source, dist))
  
  # Convert all seeds simultaneously by cutting the ranges
  metric = 'seed'
  values = seeds
  while metric != 'location':
    next_values = deque()
    while len(values) > 0:
      segment = values.popleft()
      overlap_missing = True
      for dest, source, dist in ranges[metric]:
        source_range = (source, source + dist - 1)
        overlap, nonoverlap = segment_sieve(segment, source_range)
        if overlap:
          overlap_missing = False
          for segment in nonoverlap:
            values.append(segment)
          shift = dest - source
          next_values.append((overlap[0] + shift, overlap[1] + shift))
          break
      if overlap_missing:
        next_values.append(segment)
    values = next_values
    metric = graph[metric]
  
  return min(values)[0]

# print(part1())
print(part2())
