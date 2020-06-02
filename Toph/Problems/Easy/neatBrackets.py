a = 0
for c in input():
    if c == '(':
        a += 1
    else:
        if a == 0:
            print('No')
            exit(0)
        a -= 1
print(['No', 'Yes'][a == 0])