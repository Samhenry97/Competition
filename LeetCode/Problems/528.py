from random import choices
class Solution:
    def __init__(self, w: List[int]):
        self.w = w
        self.l = list(range(len(w)))

    def pickIndex(self) -> int:
        return choices(population=self.l, weights=self.w, k=1)[0]

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()