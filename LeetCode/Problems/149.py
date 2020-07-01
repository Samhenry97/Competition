class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2: return n
        ans = 0
        for i in range(n):
            dp = defaultdict(int)
            overlap = 1
            top = 0
            for j in range(i+1, n):
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
                
                if dx == dy == 0:
                    overlap += 1
                    continue
                    
                gcd = math.gcd(dy, dx)
                dy //= gcd
                dx //= gcd
                    
                if dy == 0 and dx < 0:
                    dx *= -1
                elif dy < 0:
                    dx *= -1
                    dy *= -1
                    
                dp[(dx, dy)] += 1
                top = max(top, dp[(dx, dy)])
            ans = max(ans, top + overlap)
        return ans