class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i, n in enumerate(nums):
            if target - n not in s:
                s[n] = i
            else:
                return [s[target - n], i]
                
                