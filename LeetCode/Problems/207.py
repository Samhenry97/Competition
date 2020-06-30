class Solution:
    def dfs(self, i):
        self.vis[i] = True
        for adj in self.tree[i]:
            if self.vis[adj]:
                return True
            else:
                self.vis[adj] = True
                if self.dfs(adj):
                    return True
                self.vis[adj] = False
        return False
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.tree = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            self.tree[u].append(v)
        for i in range(numCourses):
            self.vis = [False] * numCourses
            if self.dfs(i):
                return False
        return True