class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        q = deque()
        ans = -10**20
        for x, y in points:
            while len(q) and q[0][1] < x - k:
                q.popleft()
            if len(q):
                ans = max(ans, q[0][0] + y + x)
            while len(q) and q[-1][0] <= y - x:
                q.pop()
            q.append((y - x, x))
        return ans