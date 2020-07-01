class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ans = sorted(heights)
        return len([x for i, x in enumerate(ans) if x != heights[i]])1052