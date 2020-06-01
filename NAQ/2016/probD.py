def isValid(s):
	while "()" in s:
		s = s.replace("()", "")
	return s == ""

s = input()

def opp(c):
	if c == ")":
		return "("
	return ")"

def isReal(s):
	if len(s) & 1:
		return False
	ans = ""
	isReplacing = False
	open = 0
	i = 1
	for c in s:
		#print(c, isReplacing)
		if not isReplacing:
			if c == "(":
				open += 1
			else:
				open -= 1
			if open < 0:
				isReplacing = True
				ans += opp(c)
			else:
				ans += c
		else:
			ans += opp(c)
		if isValid(ans + s[i:]):
			#print("returning true")
			return True
		i += 1
	#print("returning false")
	return False

if isReal(s):
	print("possible")
else:
	print("impossible")