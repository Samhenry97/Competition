#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> pi;
#define MAXN 1000
#define MAXK 10
#define INF INT_MAX

struct Node { int v, w; };
struct QNode { int v, w, fish; };

int n, m, k;
int shop[MAXN];
vector<Node> adj[MAXN];
int dp[MAXN][1 << MAXK];

void solve() {
    for(int i = 0; i < n; i++) fill(dp[i], dp[i] + (1 << MAXK), INF);
    queue<QNode> q;
    q.push({0, 0, shop[0]});
    dp[0][shop[0]] = 0;
    while(!q.empty()) {
        QNode &node = q.front();
        for(auto u : adj[node.v]) {
            int fish = shop[u.v] | node.fish;
            int time = u.w + node.w;
            if(time < dp[u.v][fish]) {
                dp[u.v][fish] = time;
                q.push({u.v, time, fish});
            }
        }
        q.pop();
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin >> n >> m >> k;

    for(int i = 0; i < n; i++) {
        int t; cin >> t;
        while(t--) {
            int fish; cin >> fish;
            shop[i] |= (1 << --fish);
        }
    }

    for(int i = 0; i < m; i++) {
        int a, b, w; cin >> a >> b >> w;
        adj[--a].push_back({--b, w});
        adj[b].push_back({a, w});
    }

    solve();
    int ans = INF;
    for(int i = 0; i < (1 << k); i++)
        for(int j = 0; j < (1 << k); j++)
            if((i | j) == (1 << k) - 1 and dp[n - 1][i] != INF and dp[n - 1][j] != INF)
                ans = min(ans, max(dp[n - 1][i], dp[n - 1][j]));
    cout << ans << endl;

    return 0;
}