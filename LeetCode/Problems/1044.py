from collections import defaultdict

def rabinKarp(s, m, d = 256, q = (1 << 31) - 1):
    if m == 0: return ''
    n, h, t = len(s), pow(d, m-1, q), 0
    ans = defaultdict(list)

    for i in range(m):
        t = (d * t + ord(s[i])) % q
    ans[t].append(0)

    for i in range(n - m):
        t = (d * (t - ord(s[i]) * h) + ord(s[i + m])) % q
        for j in ans[t]:
            if s[i+1:i+m+1] == s[j:j+m]:
                return s[j:j+m]
        ans[t].append(i+1)
    return ''

class Solution:
    def longestDupSubstring(self, s: str) -> str:
        bot, top = 0, len(s)
        while top - bot > 1:
            mid = (top + bot) // 2
            if rabinKarp(s, mid) != '':
                bot = mid
            else:
                top = mid - 1
        tmp1, tmp2 = rabinKarp(s, top), rabinKarp(s, bot)
        return tmp1 if tmp1 else tmp2