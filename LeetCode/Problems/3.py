class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        found = {}
        l = 0
        ans = 0
        for r, c in enumerate(s):
            if c in found:
                l = max(l, found[c])
            ans = max(ans, r - l + 1)
            found[c] = r + 1
        return ans