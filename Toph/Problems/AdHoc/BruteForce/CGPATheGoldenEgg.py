from math import floor

def points(x):
    if x >= 80:
        return 4
    elif x < 40:
        return 0
    tmp = 3.75 - 0.25 * floor((80-x)/5)
    if x % 5 == 0:
        tmp += 0.25
    return tmp
    
for i in range(int(input())):
    s = 0
    tot = 0
    fail = 0
    for _ in range(int(input())):
        n, m = input().split()
        n, m = float(n), float(m)
        p = points(n)
        tot += m
        s += p * m
        fail += p == 0
    if fail:
        print('Case {}: Sorry, you have failed in {} course{}!'.format(i+1, fail, 's' if fail > 1 else ''))
    else:
        print('Case {}: {:.2f}'.format(i+1, s / tot))
