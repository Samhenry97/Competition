class Solution:
    def findOrder(self, numCourses, prerequisites):
        self.adj = defaultdict(set)
        for u, v in prerequisites:
            self.adj[u].add(v)

        self.vis = [0] * numCourses
        self.ans, self.cycle = [], False
        
        for i in range(numCourses):
            if self.cycle: break
            if self.vis[i] == 0:
                self.dfs(i)
     
        return [] if self.cycle else self.ans

    def dfs(self, start):
        if self.cycle: return
        if self.vis[start] == 1:
            self.cycle = True
        if self.vis[start] == 0:
            self.vis[start] = 1
            for v in self.adj[start]:
                self.dfs(v)
            self.vis[start] = 2
            self.ans.append(start)
