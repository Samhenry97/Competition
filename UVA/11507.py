while True:
    try:
        n, m = int(input()), int(input())
        act = [False] * 26
        for c in input().strip():
            act[ord(c) - ord('A')] = True
        adj = [[] for i in range(26)]
        for _ in range(m):
            a, b = [ord(x) - ord('A') for x in input().strip()]
            adj[a].append(b)
            adj[b].append(a)
        steps = 0
        awake = 3
        while awake < n:
            newAct = act[:]
            for i, el in enumerate(act):
                if not el:
                    count = 0
                    for j in range(len(act)):
                        if act[j] and i in adj[j]:
                            count += 1
                    if count >= 3:
                        newAct[i] = True
                        awake += 1
            steps += 1
            if act == newAct:
                print('THIS BRAIN NEVER WAKES UP')
                break
            act = newAct[:]
        if awake == n:
            print('WAKE UP IN, {}, YEARS'.format(steps))
        input()
    except EOFError:
        break