n = int(input())

l = ['*','+','-','//']
pList = list("*+-/")

def search(num):
	for i in range(4):
		for j in range(4):
			for k in range(4):
				if eval("4" + l[i] + "4" + l[j] + "4" + l[k] + "4") == num:
					print(4, pList[i], 4, pList[j], 4, pList[k], 4, '=', num)
					return
	print("no solution")

for x in range(n):
	num = int(input())
	search(num)
