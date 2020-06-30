class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        INF = 10**16
        n, m = len(dungeon), len(dungeon[0])
        dp = [[INF] * (m+1) for _ in range(n+1)]
        dp[n-1][m], dp[n][m-1] = 1, 1
        for y in range(n-1,-1,-1):
            for x in range(m-1,-1,-1):
                dp[y][x] = max(min(dp[y+1][x], dp[y][x+1]) - dungeon[y][x], 1)
        return dp[0][0]