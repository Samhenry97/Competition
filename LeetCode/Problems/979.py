# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.ans = 0
        self.dfs(root)
        return self.ans
    
    def dfs(self, node):
        if not node: return 0
        l = self.dfs(node.left)
        r = self.dfs(node.right)
        self.ans += abs(l) + abs(r)
        return node.val + l + r - 1