class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        return ''.join([x if i & 1 else x[::-1] for i, x in enumerate([s[i*k:(i+1)*k] for i in range(math.ceil(len(s) / k))])])