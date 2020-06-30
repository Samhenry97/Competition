from collections import deque

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

class TrieNode:
    def __init__(self, parent = None, val = None):
        self.parent = parent
        self.val = val
        self.nodes = [None] * 26
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def add(self, word):
        cur = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not cur.nodes[idx]:
                cur.nodes[idx] = TrieNode(cur, c)
            cur = cur.nodes[idx]
        cur.end = True

class Solution:
    def findWords(self, board, words):
        n, m = len(board), len(board[0])
        trie = Trie()
        for word in words:
            trie.add(word)
        q = deque()
        for y in range(n):
            for x in range(m):
                idx = ord(board[y][x]) - ord('a')
                if trie.root.nodes[idx]:
                    q.append((y, x, trie.root.nodes[idx], set([(y, x)])))
        ans = set()
        while len(q):
            y, x, cur, path = q.popleft()
            if cur.end:
                word, tmp = [], cur
                while tmp.parent:
                    word.append(tmp.val)
                    tmp = tmp.parent
                ans.add(''.join(word[::-1]))
            for dy, dx in delta:
                yy, xx = y + dy, x + dx
                if 0 <= yy < n and 0 <= xx < m and (yy, xx) not in path:
                    idx = ord(board[yy][xx]) - ord('a')
                    if cur.nodes[idx]:
                        newPath = set(path)
                        newPath.add((yy, xx))
                        q.append((yy, xx, cur.nodes[idx], newPath))
        return list(ans)