s = input()
print(['No', 'Yes'][all([s[i] == s[-i-1] for i in range(len(s)//2)])])