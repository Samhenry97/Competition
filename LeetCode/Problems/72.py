def editDist(str1, str2):
    n, m = len(str1), len(str2)
    dp = [[0 for x in range(m + 1)] for x in range(n + 1)] 
    for i in range(n + 1): 
        for j in range(m + 1):
            if i == 0: 
                dp[i][j] = j
            elif j == 0: 
                dp[i][j] = i
            elif str1[i-1] == str2[j-1]: 
                dp[i][j] = dp[i-1][j-1]
            else: 
                dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
    return dp[n][m]

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return editDist(word1, word2)