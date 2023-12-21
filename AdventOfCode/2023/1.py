import re

with open('1.txt') as file:
  data = file.read().split('\n')

def part1():
  total = 0
  for line in data:
    numbers = [c for c in line if c.isdigit()]
    total += int(numbers[0] + numbers[-1])
  return total

def part2():
  total = 0
  nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
  for line in data:
    numbers = []
    for i, c in enumerate(line):
      if c.isdigit():
        numbers.append((i, c))
    for i, num in enumerate(nums):
      indices = [match.start() for match in re.finditer(num, line)]
      for start in indices:
        numbers.append((start, str(i)))
    numbers.sort()
    total += int(numbers[0][1] + numbers[-1][1])
  return total

# print(part1())
print(part2())
