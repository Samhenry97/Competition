L, R = 0, 1
for tc in range(int(input())):
    s = [int(c) for c in input()]
    n = len(s)
    par = [[0, 0] for _ in range(n)]
    for i in range(10):
        valid = [True] * n
        for c in range(n):
            if s[c] <= i:
                valid[c] = False
        vcur = False
        for c in range(n):
            if not vcur and valid[c]:
                par[c][L] += 1
                vcur = True
            elif vcur and not valid[c]:
                par[c-1][R] += 1
                vcur = False
        if vcur:
            par[n-1][R] += 1
    ans = []
    for i in range(n):
        ans.append('(' * par[i][L])
        ans.append(str(s[i]))
        ans.append(')' * par[i][R])
    print('Case #{}:'.format(tc+1), ''.join(ans))
