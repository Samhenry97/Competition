#include <bits/stdc++.h>

using namespace std;

vector<vector<int>> adj(10005);
vector<vector<int>> tree(10005);
int sizes[10005];
bool vis[10005];

void root(int curNode) {
    vis[curNode] = true;
    for(auto node : adj[curNode]) {
        if(!vis[node]) {
            tree[curNode].push_back(node);
            root(node);
        }
    }
}

void dp(int curNode) {
	sizes[curNode] = 1;
	for(auto node : tree[curNode]) {
		dp(node);
		sizes[curNode] += sizes[node];
	}
}

int main() {
	ios::sync_with_stdio(false);
	int n; scanf("%d", &n);

	for(int i = 0; i < n; i++) {
		int u, v; scanf("%d%d", &u, &v);
		adj[u].push_back(v);
		adj[v].push_back(u);
	}

	n++;
	root(0);
	dp(0);

	int maxNode = -1;
	int maxCost = -1;
	vector<int> maxSubtrees;
	for(int i = 0; i < n; i++) {
		vector<int> subtreeSizes = { sizes[0] - sizes[i] };
		for(auto node : tree[i]) {
			subtreeSizes.push_back(sizes[node]);
		}

		int cost = 0;
		for(int y = 0; y < subtreeSizes.size(); y++) {
			for(int x = y + 1; x < subtreeSizes.size(); x++) {
				cost += (subtreeSizes[y] * subtreeSizes[x]);
			}
		}

		if(cost > maxCost) {
			maxCost = cost;
			maxNode = i;
			maxSubtrees = subtreeSizes;
		}
	}

	sort(maxSubtrees.begin(), maxSubtrees.end());
	int end = maxSubtrees.size();
	maxSubtrees[end - 2] += maxSubtrees[end - 1];
	int minCost = 0;
	for(int y = 0; y < maxSubtrees.size() - 1; y++) {
		for(int x = y + 1; x < maxSubtrees.size() - 1; x++) {
			minCost += (maxSubtrees[y] * maxSubtrees[x]);
		}
	}

	printf("%d %d\n", maxCost, minCost);
}