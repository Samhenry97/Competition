# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def gen(self, n):
        if self.i >= len(self.a) or self.a[self.i] > n:
            return None
        root = TreeNode(self.a[self.i])
        self.i += 1
        root.left = self.gen(root.val)
        root.right = self.gen(n)
        return root
    
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        self.a = preorder
        self.i = 0
        if len(self.a) == 0:
            return None
        return self.gen(1e20)
        