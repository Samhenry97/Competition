class Solution:
    def dfs(self, vis, board, y, x, word, i):
        if i == len(word) - 1 and board[y][x] == word[i]: return True
        vis[y][x] = True
        if board[y][x] == word[i]:
            for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                yy, xx = y + dy, x + dx
                if 0 <= yy < len(board) and 0 <= xx < len(board[y]) and not vis[yy][xx] and self.dfs(vis, board, yy, xx, word, i + 1):
                    vis[y][x] = False
                    return True
        vis[y][x] = False
        return False
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        vis = [[False for _ in range(m)] for _ in range(n)]
        for y in range(n):
            for x in range(m):
                if self.dfs(vis, board, y, x, word, 0):
                    return True
        return False