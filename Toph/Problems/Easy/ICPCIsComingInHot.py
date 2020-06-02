from collections import Counter
c = Counter(input())
sol = max([v for v in c.values()])
print(min([k for k in c.keys() if c[k] == sol]))