class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(u):
            while adj[u]:
                dfs(adj[u].pop())
            route.append(u)
            
        route, adj = [], defaultdict(list)
        for u, v in tickets:
            adj[u].append(v)
        for u in adj:
            adj[u].sort(reverse=True)
        dfs('JFK')
        return route[::-1]