class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        cnt = {}
        cur = 0
        ans = 0
        cnt[0] = -1
        for i, n in enumerate(nums):
            cur += -1 if n == 0 else 1
            if cur in cnt:
                ans = max(ans, i - cnt[cur])
            else:
                cnt[cur] = i
        return ans
            