class Solution:
    def romanToInt(self, s: str) -> int:
        v = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
        i, ans = 0, 0
        while i < len(s):
            if i+1 < len(s) and v[s[i]] < v[s[i+1]]:
                ans += v[s[i+1]] - v[s[i]]
                i += 1
            else:
                ans += v[s[i]]
            i += 1
        return ans