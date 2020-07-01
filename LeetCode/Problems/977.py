class Solution:
    def sortedSquares(self, a: List[int]) -> List[int]:
        return sorted([n**2 for n in a])