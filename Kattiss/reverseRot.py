l = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ_.")

while True:
	data = input().split()
	if data[0] == '0': break
	rot = int(data[0])
	s = data[1]
	s = s[::-1]
	final = ""
	for c in s:
		pos = l.index(c)
		pos = (pos + rot) % len(l)
		final += l[pos]
	print(final)