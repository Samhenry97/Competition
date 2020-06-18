for t in range(int(input())):
    s, f = map(int, input().split())
    cur = 0
    ans = 'impossible'
    for i, c in enumerate(sorted(list(map(int, input().split())), reverse=True)):
        cur += c
        if cur >= s:
            ans = i + 1
            break
    print('Scenario #{}:'.format(t+1), ans, sep='\n', end='\n\n')