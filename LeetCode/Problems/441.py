class Solution:
    def arrangeCoins(self, n: int) -> int:
        ans, tot, cur = 0, 0, 1
        while tot + cur <= n:
            ans += 1
            tot += cur
            cur += 1
        return ans