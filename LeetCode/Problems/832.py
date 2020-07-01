class Solution:
    def flipAndInvertImage(self, a: List[List[int]]) -> List[List[int]]:
        for i, r in enumerate(a):
            a[i] = [x^1 for x in r[::-1]]
        return a