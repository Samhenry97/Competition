# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def dfs(node, ans):
    if node.left:
        dfs(node.left, ans)
    if node.right:
        dfs(node.right, ans)
    if not node.left and not node.right:
        ans.append(node.val)

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        a1, a2 = [], []
        if root1: dfs(root1, a1)
        if root2: dfs(root2, a2)
        return a1 == a2