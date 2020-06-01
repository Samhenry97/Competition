import sys

file = list(sys.stdin)
file = ''.join(file)

pos = 0
idt = -1
while pos < len(file):
	while pos < len(file) and file[pos] != '<':
		pos += 1
	tag = '<'
	pos += 1
	while pos < len(file) and file[pos] != '>':
		tag += file[pos]
		pos += 1
	tag += '>'
	pos += 1

	if tag[-2] == '/' or tag[1] != '/':
		idt += 1
	if len(tag) > 2: print('...' * idt + tag)
	if tag[-2] == '/' or tag[1] == '/':
		idt -= 1