input()

l = list(map(int, input().split()))

total = 0
for i in l:
	if i < 0: total += 1

print(total)