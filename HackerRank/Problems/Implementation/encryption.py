from math import sqrt, ceil

s = input()
jmp = ceil(sqrt(len(s)))
for start in range(jmp):
    for i in range(ceil(len(s) / jmp)):
        if start + jmp * i < len(s):
            print(s[start + jmp * i], end='')
    print(' ', end='')
    