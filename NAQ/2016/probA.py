newChars = ["@", "8", "(", "|)", "3", "#", "6", "[-]", "|", "_|", "|<", "1", "[]\\/[]", "[]\\[]", "0", "|D", "(,)", "|Z", "$", "']['", "|_|", "\\/", "\\/\\/", "}{", "`/", "2"]
oldChars = list("abcdefghijklmnopqrstuvwxyz")
ans = ""
for c in raw_input():
	if c.lower() in oldChars:
		pos = oldChars.index(c.lower())
		ans += newChars[pos]
	else:
		ans += c
print(ans)