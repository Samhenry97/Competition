d = [1, 2, 6]
for i in range(4, 101):
	d.append(d[i - 2] * i)

for _ in range(int(input())):
	print(d[int(input()) - 1])