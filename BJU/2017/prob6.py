vowels = 'aeiouAEIOU'
cons = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'

while True:
	try:
		data = input()
		while True:
			try:
				pos = data.index('*')
				for i in range(pos+1, len(data)):
					if not (data[i] in vowels or data[i] in cons):
						sub = data[pos:i]
						break
					if i == len(data) - 1:
						sub = data[pos:len(data)]
				word = sub
				sub = sub[1:]
				if sub[0] in vowels:
					sub = 'shm' + sub
				else:
					idx = 0
					for i, c in enumerate(sub):
						if c in vowels:
							idx = i
							break
					if idx == 0:
						sub = 'shm'
					else:
						sub = 'shm' + sub[idx:]
				data = data.replace(word, word[1:] + '-' + sub.lower())
			except ValueError:
				break
		print(data)

		# for item in line:
		# 	if item[0] == '*':
		# 		item = item[1:]
		# 		word = item
		# 		if item[0] in vowels:
		# 			item = 'shm' + item
		# 		else:
		# 			idx = 0
		# 			for i, c in enumerate(item):
		# 				if c in vowels:
		# 					idx = i
		# 					break
		# 			if idx == 0:
		# 				item = 'shm'
		# 			else:
		# 				item = 'shm' + item[idx:]
		# 		data = data.replace(word, word + '-' + item.lower())
		# print(data)

	except EOFError:
		break