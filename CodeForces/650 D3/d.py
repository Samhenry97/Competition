for _ in range(int(input())):
    s = sorted(list(input()))
    m = int(input())
    b = list(map(int, input().split()))
    found = set()
    ans = [None] * m
    while len(found) != m:
        cur = set()
        let = s[-1]
        for i, c in enumerate(b):
            if i in found:
                continue
            tot = sum([abs(i - f) for f in found] + [0])
            if tot == c and s[-1] == let:
                cur.add(i)
                ans[i] = let
        while len(s) and s[-1] == let:
            s.pop()
        found.update(cur)
    print(''.join(ans))