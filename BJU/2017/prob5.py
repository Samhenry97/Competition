text = [chr(c) for c in range(32, 123)]

while True:
	try:
		line = input()
		for c in line:
			if c in text:
				del text[text.index(c)]
	except EOFError:
		break
print(''.join(text))