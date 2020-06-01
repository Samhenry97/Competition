p = 1
max = -1

for _ in range(int(input())):
	a, b = map(int, input().split())
	if a > b:
		if a - b > max:
			max = a - b
			p = 1
	else:
		if b - a > max:
			max = b - a
			p = 2

print(p, max)