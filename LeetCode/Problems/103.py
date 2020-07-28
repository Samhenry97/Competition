# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def dfs(ans, node, lvl):
    if len(ans) <= lvl:
        ans.append([])
    ans[lvl].append(node.val)
    if node.left:
        dfs(ans, node.left, lvl + 1)
    if node.right:
        dfs(ans, node.right, lvl + 1)
        
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if root:
            dfs(ans, root, 0)
        return [x if i % 2 == 0 else x[::-1] for i, x in enumerate(ans)]