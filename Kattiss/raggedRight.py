lens = []
while True:
    try:
        lens.append(len(input()))
    except EOFError:
        break

n = max(lens)
penalty = 0
for i in range(len(lens) - 1):
    penalty += (n - lens[i])**2

print(penalty)
