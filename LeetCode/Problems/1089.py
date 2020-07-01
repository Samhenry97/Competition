class Solution:
    def duplicateZeros(self, a: List[int]) -> None:
        """
        Do not return anything, modify a in-place instead.
        """
        d, n = a.count(0), len(a)
        i = n + d - 1
        while i >= 0:
            if a[i - d] == 0:
                if i < n: a[i] = 0
                if i - 1 < n: a[i-1] = 0
                i -= 1
                d -= 1
            elif i < n:
                a[i] = a[i - d]
            i -= 1