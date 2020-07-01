class Solution:
    def replaceElements(self, a: List[int]) -> List[int]:
        top, n = -1, len(a)
        for i in range(n-1, -1, -1):
            tmp = a[i]
            a[i] = top
            top = max(top, tmp)
        return a