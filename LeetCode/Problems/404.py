# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def dfs(node, left=False):
    cur = 0
    if node.left:
        cur += dfs(node.left, True)
    if node.right:
        cur += dfs(node.right)
    if not node.left and not node.right and left:
        cur += node.val
    return cur
    
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root:
            return dfs(root)
        return 0