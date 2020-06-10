#include <queue>
#include <iostream>
#include <vector>
#include <string>
using namespace std;

int t, n, m;
vector<int> delta = { 0, 1, 1, 0, 0, -1, -1, 0 };

bool bounds(int y, int x) {
    return 0 <= y && y < n && 0 <= x && x < m;
}

int main() {
    ios::sync_with_stdio(false);

    cin >> t;
    while(t--) {
        cin >> n >> m;
        vector<string> grid(n);
        vector<vector<bool>> vis(n, vector<bool>(m, false));
        for (int y = 0; y < n; y++) cin >> grid[y];
        for (int y = 0; y < n; y++) {
            for (int x = 0; x < m; x++) {
                if (grid[y][x] == 'B') {
                    for (int i = 0; i < 4; i++) {
                        int yy = y + delta[i*2];
                        int xx = x + delta[i*2+1];
                        if (bounds(yy, xx) && grid[yy][xx] == '.') grid[yy][xx] = '#';
                    }
                }
            }
        }

        queue<pair<int, int>> q;
        if (grid[n-1][m-1] == '.') {
            q.push({ n-1, m-1 });
            vis[n-1][m-1] = true;
        }
        while (!q.empty()) {
            pair<int, int> cur = q.front(); q.pop();
            for (int i = 0; i < 4; i++) {
                int yy = cur.first + delta[i*2];
                int xx = cur.second + delta[i*2+1];
                if (bounds(yy, xx) && grid[yy][xx] != '#' && !vis[yy][xx]) {
                    vis[yy][xx] = true;
                    q.push({ yy, xx });
                }
            }
        }

        bool valid = true;
        for (int y = 0; y < n; y++) {
            for (int x = 0; x < m; x++) {
                if (grid[y][x] == 'G' && !vis[y][x]) valid = false;
                if (grid[y][x] == 'B' && vis[y][x]) valid = false;
            }
        }
        cout << (valid ? "Yes" : "No") << endl;
    }

    return 0;
}