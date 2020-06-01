n = int(input())

before = input()
after = input()

succeeded = True
for i in range(len(before)):
	if(succeeded):
		if(n & 1):
			if(before[i] == after[i]): succeeded = False
		else:
			if(before[i] != after[i]): succeeded = False

if(succeeded):
	print('Deletion succeeded')
else:
	print('Deletion failed')
