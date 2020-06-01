S, E, I = 0, 1, 2
for tc in range(int(input())):
    n = int(input())
    times = []
    for i in range(n):
        s, e = map(int, input().split())
        times.append((s, e, i))
    times.sort()
    ans = [''] * n
    cend, jend = 0, 0
    for t in times:
        if cend <= t[S]:
            cend = t[E]
            ans[t[I]] = 'C'
        elif jend <= t[S]:
            jend = t[E]
            ans[t[I]] = 'J'
        else:
            ans = ['IMPOSSIBLE']
            break
    
    print('Case #{}:'.format(tc+1), ''.join(ans))