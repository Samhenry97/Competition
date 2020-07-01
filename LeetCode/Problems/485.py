class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt, ans = 0, 0
        for n in nums:
            if n == 1:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 0
        return ans