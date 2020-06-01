s = input()
s1 = s[:len(s)//2]
s2 = s[len(s)//2:]

dist = ord('A')

rot1 = sum([ord(x) for x in s1])
rot2 = sum([ord(x) for x in s2])

es1, es2 = [], []
for c in s1:
	val = ord(c)
	val = ((val - dist) + rot1) % 26 + dist
	es1.append(chr(val))
for c in s2:
	val = ord(c)
	val = ((val - dist) + rot2) % 26 + dist
	es2.append(chr(val))

es1 = ''.join(es1)
es2 = ''.join(es2)

ans = []
for i, c in enumerate(es1):
	rot = ord(es2[i])
	val = ord(c) - dist
	val = ((val - dist) + rot) % 26 + dist
	ans.append(chr(val))
print(''.join(ans))