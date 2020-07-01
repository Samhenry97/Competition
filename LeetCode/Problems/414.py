class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        INF = -10**16
        m = max(nums)
        m2 = max([INF] + [x for x in nums if x != m])
        m3 = max([INF] + [x for x in nums if x not in [m, m2]])
        return m3 if m3 != INF else m
        