s = input()
print(len([c for c in s if c.isupper()]), len([c for c in s if c.islower()]))