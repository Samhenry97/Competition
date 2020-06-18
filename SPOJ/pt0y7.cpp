#include <iostream>
#include <vector>
using namespace std;

#define MAXN 10001

int n, m;
vector<int> adj[MAXN];
bool vis[MAXN];
int ans;

void dfs(int u) {
    ans++;
    for (auto v : adj[u]) {
        if (!vis[v]) {
            vis[v] = true;
            dfs(v);
        }
    }
}

int main() {
    ios::sync_with_stdio(false); cin.tie(0);
    cin >> n >> m;
    
    if (m != n - 1) {
        cout << "NO" << endl;
        return 0;
    }

    for (int i = 0; i < m; i++) {
        int u, v; cin >> u >> v;
        adj[--u].push_back(--v);
        adj[v].push_back(u);
    }

    vis[0] = true;
    dfs(0);

    cout << (ans == n ? "YES" : "NO") << endl;
}