n = int(input())

a = 1
b = 0
for i in range(n):
	temp = a
	a = b
	b = temp + b

print(a, b)
