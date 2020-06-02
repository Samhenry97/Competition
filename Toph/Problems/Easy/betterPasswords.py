s = input()
s = s[0].upper() + s[1:]
s = s.replace('i', '!').replace('s', '$').replace('o', '()') + '.'
print(s)