class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        tot = sum([i for i, j in costs])
        diff = sorted([j-i for i, j in costs])
        return tot + sum(diff[:len(costs)//2])