class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        return [k for k, v in c.items() if v == 1]