#include <bits/stdc++.h>
using namespace std;

#define INF 0x7FFFFFFF

typedef pair<int, int> pi;

int dijkstra(vector<vector<pi>> &adj, int src, int dest) {
	priority_queue<pi, vector<pi>, greater<pi>> q;
	vector<int> dist(adj.size(), INF);
	q.push({0, src});
	dist[src] = 0;

	while(!q.empty()) {
		int u = q.top().second; q.pop();		

		for(int i = 0; i < adj[u].size(); i++) {
			int cost = adj[u][i].first;
			int v = adj[u][i].second;

			if(dist[u] + cost < dist[v]) {
				dist[v] = dist[u] + cost;
				if(v == dest) { return dist[v]; }
				q.push({dist[v], v});
			}
		}
	}

	return dist[dest];
}

int main() {
	ios::sync_with_stdio(false);
	int q; cin >> q;

	while(q--) {
		int n, e, t, m; cin >> n >> e >> t >> m; e--;
		vector<vector<pi>> adj(n);

		for(int i = 0; i < m; i++) {
			int u, v, c; cin >> u >> v >> c;
			adj[--u].push_back({c, --v});
		}

		int count = 0;
		for(int i = 0; i < n; i++) {
			int cost = dijkstra(adj, i, e);
			if(cost <= t) { count++; }
		}

		cout << count << endl;
		if(q > 0) {
			cout << endl;
		}
	}

	return 0;
}