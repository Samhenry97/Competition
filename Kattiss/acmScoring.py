d = {}

total = 0
solved = 0

while True:
	data = input().split()
	if data[0] == '-1': break

	minute = int(data[0])
	prob = data[1]
	outcome = data[2]

	if outcome == 'right':
		if prob in d:
			total += d[prob] * 20
		total += minute
		solved += 1
	else: 
		if prob in d: d[prob] += 1
		else: d[prob] = 1

print(solved, total)