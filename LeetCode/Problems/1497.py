class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        dp = defaultdict(int)
        for n in arr:
            dp[n % k] += 1
        for n in arr:
            rem = n % k
            if rem == 0:
                if dp[0] % 2 == 1: return False
            elif dp[rem] != dp[k - rem]: return False
        return True