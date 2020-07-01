class Solution:
    def reverse(self, x: int) -> int:
        ans = int(('-' if x < 0 else '') + str(abs(x))[::-1])
        if -2 ** 31 <= ans <= 2 ** 31 - 1:
            return ans
        return 0