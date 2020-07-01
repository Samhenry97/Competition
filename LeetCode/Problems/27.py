class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ans = len(nums) - nums.count(val)
        d = 0
        for i, n in enumerate(nums):
            if n == val:
                d += 1
            else:
                nums[i - d] = nums[i]
        return ans