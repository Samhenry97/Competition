for _ in range(int(input())):
    n = int(input())
    s = list(input())
    if '_' in s:
        s.sort()
    cur, cnt = '_', 0
    valid = True
    for c in s:
        if c == cur and c != '_':
            cnt += 1
        else:
            if cur != '_' and cnt <= 1:
                valid = False
                break
            cur = c
            cnt = 1
    if cur != '_' and cnt <= 1:
        valid = False
    print(['NO', 'YES'][valid])