class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        s = Counter(arr)
        for n in arr:
            if n == 0:
                if s[0] > 1:
                    return True
            elif n * 2 in s:
                return True
        return False