#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
#include <algorithm>
#include <utility>
using namespace std;

#define INF 0x7FFFFFFF
#define MAXN 10001

int dp[MAXN];

struct cmp {
    bool operator()(const pair<int, int> &a, const pair<int, int> &b) {
        return a.second > b.second;
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(0);
    int t; cin >> t;
    while(t--) {
        int n; cin >> n;
        vector<vector<pair<int, int>>> adj(n, vector<pair<int, int>>());
        unordered_map<string, int> id;
        for (int i = 0; i < n; i++) {
            string name; cin >> name;
            id[name] = i;
            int m; cin >> m;
            for (int j = 0; j < m; j++) {
                int v, c; cin >> v >> c;
                adj[i].push_back({ --v, c });
            }
        }

        int r; cin >> r;
        while (r--) {
            fill(dp, dp + n, INF);
            string s, t; cin >> s >> t;
            int source = id[s], target = id[t];
            priority_queue<pair<int, int>, vector<pair<int, int>>, cmp> q;
            q.push({ source, 0 });
            dp[source] = 0;
            while (!q.empty()) {
                int u = q.top().first; 
                int c = q.top().second;
                q.pop();
                if (u == target) {
                    cout << c << endl;
                    break;
                }
                for (auto v : adj[u]) {
                    int cost = c + v.second;
                    if (cost < dp[v.first]) {
                        dp[v.first] = cost;
                        q.push({ v.first, cost });
                    }
                }
            }
        }
    }

    return 0;
}