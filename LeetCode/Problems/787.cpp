#define INF 10000000

struct Node {
    int u, c, k;
    bool operator<(const Node &other) const {
        return c < other.c;
    }
};

class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int K) {
        vector<vector<pair<int, int>>> adj(n, vector<pair<int, int>>());
        priority_queue<Node> q;
        vector<int> dist(n, INF);
        
        for (auto flight : flights) {
            adj[flight[0]].push_back({ flight[1], flight[2] });
        }
        
        q.push({ src, 0, 0 });
        dist[src] = 0;
        while (!q.empty()) {
            Node node = q.top(); q.pop();
            for (auto v : adj[node.u]) {
                int newC = node.c + v.second;
                if (newC < dist[v.first] && node.k <= K) {
                    dist[v.first] = newC;
                    q.push({ v.first, newC, node.k + 1 });
                }
            }
        }
        
        return dist[dst] == INF ? -1 : dist[dst];
    }
};