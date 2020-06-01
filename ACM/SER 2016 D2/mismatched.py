from collections import deque
colors = []
for _ in range(int(input())):
  colors.append(int(input()))
colors = deque(sorted(colors))

#popleft is smallest
overLeft = 0
overRight = 0
count = 0
while len(colors) > 1:
    if(len(colors) == 3):
        top = colors.pop()
        bot1 = colors.popleft()
        bot2 = colors.popleft()
        if((bot1 + bot2) > top):
            hold = (bot1 + bot2 + top) // 2
            count += hold
            break
        else:
            hold = min(top, bot1 + bot2)
            count += hold
            break
    overLeft = colors.pop()
    overRight = colors.pop()
    x = min(overLeft, overRight)
    count += x
    y = max(overLeft, overRight) - x
    if(y > 0):
        colors.append(y)
    colors = deque(sorted(colors))
print(count)
