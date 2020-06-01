n, m = map(int, input().strip().split(','))
tests = [input().strip().split('-') for _ in range(m)]

def letter(i):
    return chr(ord('A') + i)

def test(l1, l2):
    ans = []
    for test in tests:
        l, r = 0, 0
        l -= int(l1 in test[0]) + int(l2 in test[0])
        r -= int(l1 in test[1]) + int(l2 in test[1])
        if l < r:
            ans.append('L')
        elif l > r:
            ans.append('R')
        else:
            ans.append('E')
    return ans

ans = set()
for ca in range(n):
    for cb in range(ca + 1, n):
        for cc in range(ca, n):
            for cd in range(cc, n):
                if (ca == cc and cb == cd) or (ca == cb or cc == cd):
                    continue
                l1, l2, l3, l4 = map(letter, [ca, cb, cc, cd])
                if test(l1, l2) == test(l3, l4):
                    s1 = ''.join(sorted([l1, l2]))
                    s2 = ''.join(sorted([l3, l4]))
                    if s1 > s2:
                        ans.add(s2 + s1)
                    else:
                        ans.add(s1 + s2)

for item in sorted(list(ans)):
    print('{}={}'.format(item[:2], item[2:]))