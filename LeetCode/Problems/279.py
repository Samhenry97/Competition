class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] + [10**6] * (n)
        sq = []
        for i in range(1, n+1):
            if i * i <= n:
                sq.append(i * i)
            for s in sq:
                if s <= i:
                    dp[i] = min(dp[i], dp[i - s] + 1)
                else:
                    break
        return dp[n]