import math

with open('6.txt') as file:
  data = file.read().split('\n')

def part1():
  time = [int(x) for x in data[0].split()[1:]]
  dist = [int(x) for x in data[1].split()[1:]]

  races = len(time)
  results = []
  for race in range(races):
    result = 0
    for windup in range(time[race]):
      if windup * (time[race] - windup) > dist[race]:
        result += 1
    results.append(result)
  
  return math.prod(results)

def part2():
  def search(lo, hi, time, dist, asc):
    while hi - lo > 1:
      mid = (hi + lo) // 2
      good = mid * (time - mid) > dist
      if good == asc:
        hi = mid
      else:
        lo = mid
    return lo

  time = int(''.join(data[0].split()[1:]))
  dist = int(''.join(data[1].split()[1:]))

  left = search(0, time // 2, time, dist, True)
  right = search(time // 2, time, time, dist, False)
  return right - left

# print(part1())
print(part2())
