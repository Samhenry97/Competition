from bisect import bisect_left

def pal(s):
    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            return False
    return True

poss = set()
for i in range(100, 1000):
    for j in range(100, 1000):
        prod = i * j
        if pal(str(prod)):
            poss.add(prod)
ans = sorted(poss)

for _ in range(int(input())):
    print(ans[bisect_left(ans, int(input()))-1])