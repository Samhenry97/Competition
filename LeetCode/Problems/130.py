class Solution:
    def search(self, board, vis, n, m, sy, sx):
        delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = [(sy, sx)]
        qi = 0
        vis[sy][sx] = True
        while qi < len(q):
            y, x = q[qi]
            for d in delta:
                yy, xx = y + d[0], x + d[1]
                if 0 <= yy < n and 0 <= xx < m and board[yy][xx] == 'O' and not vis[yy][xx]:
                    vis[yy][xx] = True
                    q.append((yy, xx))
            qi += 1
    
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        if n == 0: return
        m = len(board[0])
        vis = [[False for _ in range(m)] for _ in range(n)]
        for i in range(n):
            if not vis[i][0] and board[i][0] == 'O':
                self.search(board, vis, n, m, i, 0)
            if not vis[i][-1] and board[i][-1] == 'O':
                self.search(board, vis, n, m, i, m-1)
        for i in range(m):
            if not vis[0][i] and board[0][i] == 'O':
                self.search(board, vis, n, m, 0, i)
            if not vis[-1][i] and board[-1][i] == 'O':
                self.search(board, vis, n, m, n-1, i)
        for y in range(n):
            for x in range(m):
                if not vis[y][x] and board[y][x] == 'O':
                    board[y][x] = 'X'