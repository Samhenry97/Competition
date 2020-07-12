class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 1000000007
        path = [(4, 6), (6, 8), (7, 9), (4, 8), (3, 9, 0), (), (1, 7, 0), (2, 6), (1, 3), (2, 4)]
        dp = [[0 for _ in range(10)] for _ in range(n+1)]
        dp[1] = [1 for _ in range(10)]
        for i in range(2, n+1):
            for j in range(10):
                for p in path[j]:
                    dp[i][j] = (dp[i][j] + dp[i-1][p]) % MOD
        return sum(dp[n]) % MOD