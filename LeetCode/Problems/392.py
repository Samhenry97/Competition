import re
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pat = '.*' + '.*'.join(list(s)) + '.*'
        return bool(re.match(pat, t))