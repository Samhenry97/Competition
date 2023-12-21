from collections import Counter
from functools import cmp_to_key

with open('7.txt') as file:
  data = file.read().split('\n')

def part1():
  order = {c: i for i, c in enumerate('23456789TJQKA')}

  def compare(h1, h2):
    c1 = sorted(Counter(h1[0]).values())
    c2 = sorted(Counter(h2[0]).values())
    if c1 == c2:
      for t1, t2 in zip(h1[0], h2[0]):
        if t1 != t2:
          return order[t1] - order[t2]
    elif len(c1) == len(c2):
      return c1[-1] - c2[-1]
    elif len(c1) < len(c2):
      return 1
    return -1

  hands = []
  for line in data:
    hand, bid = line.split()
    hands.append((hand, int(bid)))
  hands.sort(key=cmp_to_key(compare))
  
  ans = 0
  for i, hand in enumerate(hands):
    ans += hand[1] * (i + 1)
  return ans

def part2():
  order = {c: i for i, c in enumerate('J23456789TQKA')}

  def compare(h1, h2):
    c1 = sorted(Counter((c for c in h1[0] if c != 'J')).values())
    c2 = sorted(Counter((c for c in h2[0] if c != 'J')).values())
    if len(c1) == 0:
      c1.append(0)
    if len(c2) == 0:
      c2.append(0)
    c1[-1] += 5 - sum(c1)
    c2[-1] += 5 - sum(c2)
    
    if c1 == c2:
      for t1, t2 in zip(h1[0], h2[0]):
        if t1 != t2:
          return order[t1] - order[t2]
    elif len(c1) == len(c2):
      return c1[-1] - c2[-1]
    elif len(c1) < len(c2):
      return 1
    return -1
  
  hands = []
  for line in data:
    hand, bid = line.split()
    hands.append((hand, int(bid)))
  hands.sort(key=cmp_to_key(compare))
  
  ans = 0
  for i, hand in enumerate(hands):
    ans += hand[1] * (i + 1)
  return ans

# print(part1())
print(part2())
