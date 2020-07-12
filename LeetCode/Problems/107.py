# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def dfs(node, ans, lvl):
    if len(ans) <= lvl:
        ans.append([])
    ans[lvl].append(node.val)
    if node.left:
        dfs(node.left, ans, lvl + 1)
    if node.right:
        dfs(node.right, ans, lvl + 1)

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if root: dfs(root, ans, 0)
        return ans[::-1]