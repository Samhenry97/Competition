class Solution:
    def hIndex(self, citations: List[int]) -> int:
        tmp = [i + c >= len(citations) for i, c in enumerate(citations)][::-1] + [0]
        return tmp.index(0)