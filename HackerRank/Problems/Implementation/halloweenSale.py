p, d, m, s = map(int, input().split())
if p > s: print(0); exit()
t = (p - m) // d
g = 1
s -= p * (t + 1) - d * ((t * (t + 1)) // 2)
if s >= 0: g += t; g += s // m
print(g)