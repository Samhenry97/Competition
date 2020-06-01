class Node:
	def __init__(self):
		self.down = False
		self.right = False

	def __repr__(self):
		return str(self.down) + str(self.right)

num = 0
while True:
	num += 1
	try:
		dots = int(input())
		if num != 1:
			print('**********')
		count = [0] * (dots - 1)
		nodes = [[Node() for _ in range(dots)] for _ in range(dots)]
		for _ in range(int(input())):
			data = input().split()
			row = int(data[1]) - 1
			col = int(data[2]) - 1
			if data[0] == 'H':
				nodes[row][col].right = True
			else:
				nodes[row][col].down = True

		for size in range(1, dots):
			for xstart in range(dots - size):
				for ystart in range(dots - size):
					valid = True
					for x in range(size):
						if not nodes[ystart][xstart + x].right: #top 
							valid = False
						if not nodes[ystart + size][xstart + x].right: #bottom
							valid = False
						if not nodes[ystart + x][xstart].down: #left
							valid = False
						if not nodes[ystart + x][xstart + size].down: #right
							valid = False
					if valid:
						count[size - 1] += 1

		print('Problem #{}'.format(num))
		for i, c in enumerate(count):
			print('size {} = {}'.format(i + 1, c))
	except EOFError:
		break