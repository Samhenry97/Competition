inp = list(map(int, input().split()))
data = [(a, b) for a, b in zip(inp[::2], inp[1::2])]

mac = []
for _ in range(10):
	mac.append(list(map(int, input().split())))

time = 0
for i in range(3):
	for m in range(10):
		if time + data[m][0] < sum(mac[m]):
			time = sum(mac[m])
		elif time <= sum(mac[m]):
			time = sum(mac[m])
		time += sum(data[m])
print(time - data[-1][1])