#include <bits/stdc++.h>
using namespace std;

#define MAXN 500
#define INF 0x7FFFFFFF

typedef long long int ll;

struct Node {
    int y, x, cost;
    bool operator<(const Node &other) const {
        return cost > other.cost;
    }
};

int grid[MAXN][MAXN];
int dp[MAXN][MAXN];
int delta[] = { -1, 0, 0, -1, 1, 0, 0, 1 };

int main() {
    int n, m; cin >> n >> m;
    for (int y = 0; y < n; y++) {
        for (int x = 0; x < m; x++) {
            cin >> grid[y][x];
            dp[y][x] = INF;
        }
    }
    
    priority_queue<Node> q;
    q.push({ 0, 0, 0 });
    dp[0][0] = 0;
    while (!q.empty()) {
        Node cur = q.top(); q.pop();
        int y = cur.y, x = cur.x, cost = cur.cost;
        for (int i = 0; i < 4; i++) {
            int yy = y + delta[i*2];
            int xx = x + delta[i*2+1];
            if (0 <= yy && yy < n && 0 <= xx && xx < m) {
                int newCost = max(cost, abs(grid[yy][xx] - grid[y][x]));
                if (newCost < dp[yy][xx]) {
                    dp[yy][xx] = newCost;
                    q.push({ yy, xx, newCost });
                }
            }
        }
    }
    
    cout << dp[n-1][m-1] << endl;
    
    return 0;
}
