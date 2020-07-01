class Solution:
    def validMountainArray(self, a: List[int]) -> bool:
        if len(a) == 0: return False
        s, n = a.index(max(a)), len(a)
        if s == 0 or s == n - 1:
            return False
        for i in range(s + 1, n):
            if a[i] >= a[i-1]:
                return False
        for i in range(s - 1, -1, -1):
            if a[i] >= a[i+1]:
                return False
        return True