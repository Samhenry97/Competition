for _ in range(int(input())):
	s = list(map(int, input().strip().lstrip('0')))
	if all([c == 9 for c in s]):
		print('1{}1'.format('0' * (len(s) - 1)))
		continue
	mid = len(s) // 2
	i = mid if len(s) % 2 else mid - 1
	while i >= 0 and s[i] == s[-i-1]:
		i -= 1
	if i < 0 or s[i] < s[-i-1]:
		carry = 1
		i = mid if len(s) % 2 else mid - 1
		while i >= 0:
			s[i] += carry
			carry = s[i] // 10
			s[i] %= 10
			s[-i-1] = s[i]
			i -= 1
	else:
		while i >= 0:
			s[-i-1] = s[i]
			i -= 1
	print(''.join(map(str, s)))