n, k = map(int, input().split())
data = input().split()
idx = 0
pos = 0
stack = []
for i in range(k):
	if data[idx] == 'undo':
		amt = int(data[idx+1])
		pos = stack[-amt-1]
		stack = stack[:-amt]
		idx += 2
	else:
		amt = int(data[idx])
		pos += amt
		pos %= n
		stack.append(pos)
		idx += 1
print(pos)