s = input()
while s != '0':
	print('{} is {}a multiple of 11.'.format(s, '' if int(s) % 11 == 0 else 'not '))
	s = input()