for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    good = [False] * n
    for i in range(1, n-1):
        good[i] = s[i-1] < s[i] and s[i] > s[i+1]
    if len(set(s)) == 1:
        print('neutral')
    elif sorted(s) == s:
        print('allGoodDays')
    elif sorted(s, reverse=True) == s:
        print('allBadDays')
    elif good.count(True) < 2:
        print('none')
    else:
        st = good.index(True)
        cnt = 0
        ans = 0
        for i in range(st+1, n):
            if not good[i]:
                cnt += 1
            else:
                ans = max(ans, cnt)
                cnt = 0
        print(ans)