import sys

for s in sys.stdin:
    s = s.strip()
    if s.lower() != s: # Java
        if '_' in s or s[0].isupper():
            print('Error!')
            continue
        ans = []
        for c in s:
            if c.islower():
                ans.append(c)
            else:
                ans.extend(['_', c.lower()])
        print(''.join(ans))
    else: # C++
        data = s.split('_')
        if '' in data:
            print('Error!')
            continue
        print(''.join([data[0]] + [c[0].upper() + c[1:] for c in data[1:]]))