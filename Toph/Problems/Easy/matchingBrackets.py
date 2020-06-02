s = []
valid = True
for c in input():
    if c in '[({':
        s.append(c)
    elif len(s) == 0:
        valid = False
    elif s[-1] == '[':
        if c != ']':
            valid = False
        s.pop()
    elif s[-1] == '(':
        if c != ')':
            valid = False
        s.pop()
    elif s[-1] == '{':
        if c != '}':
            valid = False
        s.pop()
    if not valid:
        break
print(['No', 'Yes'][valid and len(s) == 0])