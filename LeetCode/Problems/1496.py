class Solution:
    def isPathCrossing(self, path: str) -> bool:
        y, x = 0, 0
        found = set([(0, 0)])
        delta = { 'N': (1, 0), 'S': (-1, 0), 'E': (0, 1), 'W': (0, -1) }
        for c in path:
            y += delta[c][0]
            x += delta[c][1]
            if (y, x) in found:
                return True
            found.add((y, x))
        return False