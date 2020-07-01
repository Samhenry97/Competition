class Solution:
    def sortArrayByParity(self, a: List[int]) -> List[int]:
        n = len(a)
        i, j = 0, n - 1
        while i < j:
            while a[i] % 2 == 1 and i < j:
                a[i], a[j] = a[j], a[i]
                j -= 1
            i += 1
        return a