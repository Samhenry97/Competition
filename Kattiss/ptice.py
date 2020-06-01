input()
s = input()

adrian = list("ABC")
brun = list("BABC")
goran = list("CCAABB")

aRight = 0
bRight = 0
gRight = 0
for i in range(len(s)):
	if s[i] == adrian[i % len(adrian)]: aRight += 1
	if s[i] == brun[i % len(brun)]: bRight += 1
	if s[i] == goran[i % len(goran)]: gRight += 1

total = max(aRight, bRight, gRight)

finals = list()
if aRight == total:
	finals.append("Adrian")
if bRight == total:
	finals.append("Bruno")
if gRight == total:
	finals.append("Goran")

print(total)
for i in finals:
	print(i)
