# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def dfs(u, v):
    if u == v == None:
        return True
    elif u == None or v == None:
        return False
    return u.val == v.val and dfs(u.left, v.left) and dfs(u.right, v.right)

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return dfs(p, q)