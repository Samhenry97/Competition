n = int(input())

l = list()
for i in range(n):
	l.append(input())

newList = sorted(l)
backList = sorted(l, reverse=True)
if newList == l:
	print("INCREASING")
elif backList == l:
	print("DECREASING")
else:
	print("NEITHER")
