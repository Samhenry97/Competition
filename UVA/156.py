l = input().strip()
words, orig = {}, {}
while l != '#':
	data = l.split()
	for word in data:
		actual = ''.join(sorted(list(word.lower())))
		orig[actual] = word
		words[actual] = actual not in words
	l = input().strip()
ans = [orig[k] for k, v in words.items() if v]
print('\n'.join(sorted(ans)))