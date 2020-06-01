#include <bits/stdc++.h>

using namespace std;

int n, m;
bool vis[501];
vector<vector<int>> adjIs(501);
vector<vector<int>> adj(501);

bool dfsIs(int src, int tar) {
	for(int i = 0; i < adjIs[src].size(); i++) {
		int u = adjIs[src][i];
		if(u == tar) { return true; }
		else if(dfsIs(u, tar)) { return true; }
	}
	return false;
}

bool dfs(int src, int tar) {
	vis[src] = true;
	for(int i = 0; i < adj[src].size(); i++) {
		int u = adj[src][i];
		if(u == tar) { return true; }
		if(!vis[u] && dfs(u, tar)) { return true; }
	}
	vis[src] = false;
	return false;
}

int main() {
	cin >> n >> m;
	map<string, int> nodes;
	int idx = 0;

	while(n--) {
		string a, v, b; cin >> a >> v >> b;
		if(nodes.find(a) == nodes.end()) { nodes[a] = idx++; }
		if(nodes.find(b) == nodes.end()) { nodes[b] = idx++; }
		if(v == "is-a") { adjIs[nodes[a]].push_back(nodes[b]); }
		adj[nodes[a]].push_back(nodes[b]);
	}

	for(int i = 0; i < m; i++) {
		string a, v, b; cin >> a >> v >> b;
		fill(vis, vis + 501, false);
		if(v == "is-a" && nodes[a] == nodes[b]) {
			printf("Query %d: true\n", i + 1);
		} else if(v == "is-a") {
			printf("Query %d: %s\n", i + 1, dfsIs(nodes[a], nodes[b]) ? "true" : "false");
		} else {
			printf("Query %d: %s\n", i + 1, (dfs(nodes[a], nodes[b]) && !dfsIs(nodes[a], nodes[b])) ? "true" : "false");
		}
	}

	return 0;
}