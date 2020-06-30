# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def dfs(node, tot):
    tot = tot * 10 + node.val
    if not (node.left or node.right):
        return tot
    cur = 0
    if node.left:
        cur += dfs(node.left, tot)
    if node.right:
        cur += dfs(node.right, tot)
    return cur

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root: return 0
        return dfs(root, 0)