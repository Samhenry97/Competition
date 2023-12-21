with open('4.txt') as file:
  data = file.read().split('\n')

def part1():
  ans = 0
  for card in data:
    left, right = card.split(':')[1].split('|')
    winning = {int(x) for x in left.split()}
    matches = 0
    for yours in right.split():
      if int(yours) in winning:
        matches += 1
    if matches > 0:
      ans += 2 ** (matches - 1)
  return ans

def part2():
  scores = []
  for card in data:
    left, right = card.split(':')[1].split('|')
    winning = {int(x) for x in left.split()}
    matches = 0
    for yours in right.split():
      if int(yours) in winning:
        matches += 1
    scores.append(matches)
  copies = [1] * len(scores)
  for i in range(len(scores)):
    for j in range(1, min(scores[i] + 1, len(scores))):
      copies[i + j] += copies[i]
  return sum(copies)

# print(part1())
print(part2())
