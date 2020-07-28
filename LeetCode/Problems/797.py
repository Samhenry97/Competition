def dfs(ans, tmp, adj, u):
    if u == len(adj) - 1:
        ans.append(tmp[:] + [u])
    tmp.append(u)
    for v in adj[u]:
        dfs(ans, tmp, adj, v)
    tmp.pop()

class Solution:
    def allPathsSourceTarget(self, adj: List[List[int]]) -> List[List[int]]:
        ans, tmp = [], []
        dfs(ans, tmp, adj, 0)
        return ans