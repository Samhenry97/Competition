import math

def log(x):
	return math.log(x, 10)

def factLen(n):
	return round(log(math.sqrt(2 * math.pi * n)) + n * log(n / math.e) + 1 / (12 * n) * log(math.e))

s = input()
l = len(s)

if l < 1000:
	divisor = 1
	n = int(s)
	while n > 1:
		n //= divisor
		divisor += 1
	print(divisor - 1)
else:
	low = 0
	hi = 10 ** 6

	mid = (low + hi) // 2
	l2 = factLen(mid)
	while abs(l2 - l) > 1:
		if l2 > l:
			hi = mid
			mid = (low + hi) // 2
			l2 = factLen(mid)
		else:
			low = mid
			mid = (low + hi) // 2
			l2 = factLen(mid)
	print(mid)