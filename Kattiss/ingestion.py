n, c = map(int, input().split())
cals = list(map(int, input().split()))

maxCals = -1
def calc(idx, consumed, cur):
	global maxCals
	if idx == n:
		if sum(consumed) > maxCals:
			maxCals = sum(consumed)
		return

	if len(consumed) >= 2 and sum(consumed[-2:]) == 0: # Didn't eat two meals
		consumed.append(min(cals[idx], c))
		calc(idx + 1, consumed, c)
		consumed.pop()
	else:
		consumed.append(min(cals[idx], cur))
		calc(idx + 1, consumed, int(cur * (2 / 3)))
		consumed.pop()

		consumed.append(0)
		calc(idx + 1, consumed, cur)
		consumed.pop()
		
calc(0, [], c)
print(maxCals)