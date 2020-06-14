#include <iostream>
#include <vector>
#include <queue>
#include <cstring>
using namespace std;

#define MAXN 5007

int n, m;
int n1, n2, n3;
vector<int> adj[MAXN];
vector<vector<int>> conn[2];
int col[MAXN];
bool ans[MAXN];
int dp[MAXN][MAXN];

bool bipartite(int root) {
    conn[0].push_back(vector<int>());
    conn[1].push_back(vector<int>());
    col[root] = 0;
    queue<int> q;
    q.push(root);
    while (!q.empty()) {
        int u = q.front(); q.pop();
        conn[col[u]].back().push_back(u);
        for (int v : adj[u]) {
            if (col[v] == -1) {
                col[v] = !col[u];
                q.push(v);
            } else if (col[v] == col[u]) return false;
        }
    }
    return true;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(0);
    cin >> n >> m >> n1 >> n2 >> n3;
    for (int i = 0; i < m; i++) {
        int u, v; cin >> u >> v;
        adj[--u].push_back(--v);
        adj[v].push_back(u);
    }

    memset(col, -1, sizeof(col));
    for (int i = 0; i < n; i++) {
        if (col[i] == -1 && !bipartite(i)) {
            cout << "NO" << endl;
            return 0;
        }
    }

    memset(dp, -1, sizeof(dp));
    dp[0][0] = 0;
    for (int i = 0; i < conn[0].size(); i++) {
        for (int j = 0; j < n; j++) {
            if (dp[i][j] != -1) {
                dp[i+1][j+conn[0][i].size()] = 0;
                dp[i+1][j+conn[1][i].size()] = 1;
            }
        }
    }

    if (dp[conn[0].size()][n2] == -1) {
        cout << "NO" << endl;
        return 0;
    }

    int tot = n2;
    for (int i = conn[0].size(); i > 0; i--) {
        for (int v : conn[dp[i][tot]][i-1]) ans[v] = true;
        tot -= conn[dp[i][tot]][i-1].size();
    }

    cout << "YES" << endl;
    for (int i = 0; i < n; i++) {
        if (ans[i]) cout << 2;
        else if (n1-- > 0) cout << 1;
        else cout << 3;
    }
    cout << endl;
    
    return 0;
}