class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums) == 0: return []
        nums.sort()
        dp = [[a] for a in nums]
        for i, a in enumerate(nums):
            for j in range(i):
                if a % nums[j] == 0 and len(dp[i]) < len(dp[j]) + 1:
                    dp[i] = dp[j] + [a]
        return max(dp, key=len)
                