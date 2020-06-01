olivia = input()
while olivia != '0':
	sum = 0
	for c in olivia:		#sum all of the digits
		sum += int(c)
	olivia = int(olivia) 	#change sum to integer

	for i in range(11, 10000):
		temp = 0
		for c in str(i * olivia):
			temp += int(c)
		if temp == sum:
			print(i)
			break

	olivia = input()
