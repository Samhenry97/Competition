#include <iostream>
#include <vector>
#include <queue>
#include <set>
using namespace std;

int main() {
    int t; cin >> t;
    while(t--) {
        int n, m; cin >> n >> m;
        vector<vector<int>> adj(n, vector<int>());
        vector<bool> vis(n, false);
        set<int> ans;
        for (int i = 0; i < m; i++) {
            int u, v; cin >> u >> v;
            adj[--u].push_back(--v);
        }
        queue<pair<int, int>> q;
        for (int i = 0; i < n; i++) {
            if (vis[i]) continue;
            q.push({ i, 0 });
            while (!q.empty()) {
                int u = q.front().first;
                int d = q.front().second;
                q.pop();
                if (d % 3 == 0) ans.insert(u);
                for (int v : adj[u]) {
                    vis[v] = true;
                    q.push({ v, d + 1 });
                }
            }
        }
        cout << ans.size() << endl;
        for (auto u : ans) cout << u + 1 << " ";
        cout << endl;
    }

    return 0;
}