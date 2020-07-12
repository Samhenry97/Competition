class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ans = 0
        for y in range(n):
            for x in range(m):
                if grid[y][x] == 0: continue
                for dy, dx in delta:
                    yy, xx = y + dy, x + dx
                    if xx < 0 or yy < 0 or xx >= m or yy >= n or grid[yy][xx] == 0:
                        ans += 1
        return ans