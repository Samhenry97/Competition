n = int(input())
x = [0] * 100001
v = [0] * 100001

for i in range(n):
	x[i], v[i] = map(float, input().split())
	
def span(time):
	left, right = float('inf'), -float('inf')
	for i in range(n):
		pos = x[i] + time * v[i]
		left = min(left, pos)
		right = max(right, pos)
	return right - left

prev, low, high = None, 0.0, 200000.0
while True:
	lmid = (2 * low + high) / 3
	rmid = (low + 2 * high) / 3
	lres = span(lmid)
	rres = span(rmid)
	if lres > rres:
		low = lmid
	else:
		high = rmid
	if prev != None and abs(prev - lres) < 0.0001:
		break
	prev = lres

print('{0:.4f}'.format(prev))