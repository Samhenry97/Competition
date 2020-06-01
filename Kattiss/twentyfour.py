from itertools import permutations, combinations
import re

div = re.compile('(?=([0-9]+ */ *[0-9]+))')

paren = [
	'# & # & # & #',
	'(# & # & #) & #',
	'((# & #) & #) & #',
	'(# & (# & #)) & #',
	'# & (# & # & #)',
	'# & ((# & #) & #)',
	'# & (# & (# & #))',
	'(# & #) & # & #',
	'(# & #) & (# & #)',
	'# & # & (# & #)',
	'# & (# & #) & #'
]

def inv(orig, perm):
	count = 0
	for i in range(len(orig) - 1):
		loc = perm[i:].index(orig[i]) + i
		while loc != i:
			perm[loc], perm[loc - 1] = perm[loc - 1], perm[loc]
			count += 2
			loc = perm[i:].index(orig[i]) + i
	return count

minCost = -1

def test(perm, l, invCount):
	global minCost, best
	for exp in paren:
		poss = exp
		for op in perm:
			poss = poss.replace('&', op, 1)
		for num in l:
			poss = poss.replace('#', num, 1)
		try:
			if eval(poss) == 24:
				if eval(poss) == eval(poss.replace('/', '//')):
					cost = poss.count('(') + invCount
					if cost < minCost or minCost == -1:
						minCost = cost
						best = poss
		except Exception as e:
			pass

def operatorPerms(l, invCount):
	ops = ['+', '-', '*', '/']
	for x in range(4):
		for y in range(4):
			for z in range(4):
				perm = [ops[x], ops[y], ops[z]]
				test(perm, l, invCount)

def numPerms(l):
	for perm in permutations(l):
		perm = list(perm)
		invCount = inv(l, perm[:])
		operatorPerms(perm, invCount)

orig = input().split()
numPerms(orig)
print(minCost if minCost != -1 else 'impossible')