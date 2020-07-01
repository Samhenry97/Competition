class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n, INF = len(cost), 10**9
        dp = [0, 0] + [INF] * n
        for i in range(n):
            for j in range(1, 3):
                dp[i+j] = min(dp[i+j], dp[i] + cost[i])
        return dp[n]