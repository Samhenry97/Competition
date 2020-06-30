# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def dfs(root, tree):
    if root.left:
        tree.right = TreeNode(root.left.val)
        dfs(root.left, tree.right)
    if root.right:
        tree.left = TreeNode(root.right.val)
        dfs(root.right, tree.left)

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        tree = TreeNode(root.val)
        dfs(root, tree)
        return tree