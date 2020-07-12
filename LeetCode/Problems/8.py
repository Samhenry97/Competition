class Solution:
    def myAtoi(self, s: str) -> int:
        s, ans = list(s.lstrip()), []
        if not len(s): return 0
        if s[0] in '-+':
            ans.append(s.pop(0))
        for c in s:
            if c.isnumeric():
                ans.append(c)
            else:
                break
        if not len(ans) or ans in [['-'], ['+']]:
            return 0
        tmp = int(''.join(ans))
        if tmp < -2**31:
            tmp = -2**31
        elif tmp >= 2**31:
            tmp = 2**31-1
        return tmp
        