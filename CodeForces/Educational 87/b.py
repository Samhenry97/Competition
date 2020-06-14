for _ in range(int(input())):
    s = input()
    rng = []
    start, cur = 0, s[0]
    for i in range(1, len(s)):
        if cur != s[i]:
            rng.append((start, i))
            start = i
            cur = s[i]
    ans = 200001
    for l, r in rng:
        if 0 < l and r < len(s):
            if s[l-1] != s[r]:
                ans = min(ans, r - l + 2)
    print(ans if ans != 200001 else 0)