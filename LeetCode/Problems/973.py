from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key=lambda p: sqrt(p[0]**2+p[1]**2))
        return points[:K]