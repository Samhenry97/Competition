#include <bits/stdc++.h>
using namespace std;

int n, m, ans = 0, minPath = 999999;
vector<int> adj[36];
int g[36];
bool v[36];
bool v2[36];
bool s[36];

void dfsBack(int cur, int sum, int path) {
	if(path > minPath) { return; }
	if(path == minPath && sum <= ans) { return; }
	if(cur == 0) { 
		if(path < minPath) { 
			ans = sum;
			minPath = path;
		} else if(path == minPath) {
			ans = max(ans, sum);
		}
		return; 
	}
	v2[cur] = true;
	for(auto u : adj[cur]) {
		if(!v2[u] && !s[u]) {
			dfsBack(u, sum, path);
		}
	}
	v2[cur] = false;
}

void dfs(int cur, int sum, int path) {
	if(path > minPath) { return; }
	if(cur == 1) { dfsBack(cur, sum, path); return; }

	v[cur] = true;
	for(auto u : adj[cur]) {
		if(v[u]) { continue; }
		if(cur != 0) {
			s[cur] = true;
			dfs(u, sum + g[cur - 2], path + 1);
			s[cur] = false;
		}
		dfs(u, sum, path + 1);
	}
	v[cur] = false;
}

struct Node {
	int v, sum, path;
	int stole[36];
	int vis[36];
};

int main() {
	ios::sync_with_stdio(false);
	scanf("%d%d", &n, &m);
	for(int i = 0; i < n - 2; i++) { scanf("%d", g + i); }
	for(int i = 0; i < m; i++) {
		int a, b; scanf("%d%d", &a, &b);
		adj[--a].push_back(--b);
		adj[b].push_back(a);
	}

	queue<Node> q;
	q.push({0});
	while(!q.empty()) {
		Node node = q.front();
		for(auto u : adj[v]) {
			if(node.vis.)
		}
	}


	dfs(0, 0, 0);
	cout << ans << endl;

	return 0; 
}