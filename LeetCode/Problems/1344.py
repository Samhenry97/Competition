class Solution:
    def angleClock(self, h: int, m: int) -> float:
        h = (h/12)*360 + m/60*1/12*360
        m = (m/60)*360
        ans = abs(h-m)
        ans = min(ans, 360-ans)
        return ans