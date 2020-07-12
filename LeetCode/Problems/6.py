class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = [[] for _ in range(numRows)]
        cur, dir = 0, 1 if numRows > 1 else 0
        for c in s:
            ans[cur].append(c)
            cur += dir
            if cur == 0 and dir == -1:
                dir = 1
            elif cur == numRows - 1 and dir == 1:
                dir = -1
        return ''.join([''.join(row) for row in ans])