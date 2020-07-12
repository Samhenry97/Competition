# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

INF = pow(10, 1000)

def dfs(node, id, lvl, ans):
    if len(ans) <= lvl:
        ans.append([INF, -INF])
    ans[lvl][0] = min(ans[lvl][0], id)
    ans[lvl][1] = max(ans[lvl][1], id)
    if node.left:
        dfs(node.left, id * 2, lvl + 1, ans)
    if node.right:
        dfs(node.right, id * 2 + 1, lvl + 1, ans)

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0
        ans = []
        dfs(root, 1, 0, ans)
        return max([x[1] - x[0] + 1 for x in ans])