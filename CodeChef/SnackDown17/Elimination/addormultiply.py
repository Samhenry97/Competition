for _ in range(int(input())):
	n = int(input())
	l = [int(x) for x in input().split()]
	times = n - 1
	plus = 2 ** (n - 2)
	print(times, plus)
	total = l[0] * plus + (l[0] * l[1]) * times
	for i in range(1, n - 1):
		total += (l[i] * l[i + 1]) * times
		total += l[i] * (plus - 1)
	total += l[-1] * plus
	total += (l[-1] * l[-2]) * times
	print(total)