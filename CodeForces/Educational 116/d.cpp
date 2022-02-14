#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

bool sortcol(const vector<int>& a, const vector<int>& b) {
    for (int i = 0; i < a.size(); i++) {
        if (a[i] != b[i]) {
            return a[i] < b[i];
        }
    }
    return true;
}

int main() {
    int t; cin >> t;

    while(t--) {
        // Initialize
        int n, m; cin >> n >> m;
        vector<vector<int>> grid(n, vector<int>(m, 0));
        vector<vector<int>> maxTLdp(n, vector<int>(m, 0));
        vector<vector<int>> minTRdp(n, vector<int>(m, 0));
        vector<vector<int>> minBLdp(n, vector<int>(m, 0));
        vector<vector<int>> maxBRdp(n, vector<int>(m, 0));

        // Read in data
        for (int y = 0; y < n; y++) {
            for (int x = 0; x < m; x++) {
                cin >> grid[y][x];
            }
        }

        // Sort and compute indices
        vector<int> idx(n);
        vector<int> idxcopy(n);
        iota(idx.begin(), idx.end(), 0);
        stable_sort(idx.begin(), idx.end(), [&grid](int a, int b) {
            return sortcol(grid[a], grid[b]);
        });
        stable_sort(grid.begin(), grid.end(), sortcol);
        for (int i = 0; i < n; i++) {
            idxcopy[idx[i]] = i;
        }

        // Compute min/max prefix matrices
        for (int y = 0; y < n; y++) {
            for (int x = 0; x < m; x++) {
                maxTLdp[y][x] = grid[y][x];
                if (x > 0) maxTLdp[y][x] = max(maxTLdp[y][x], grid[y][x-1]);
                if (y > 0) maxTLdp[y][x] = max(maxTLdp[y][x], grid[y-1][x]);
            }
        }
        for (int y = 0; y < n; y++) {
            for (int x = m - 1; x >= 0; x--) {
                minTRdp[y][x] = grid[y][x];
                if (x < m - 1) minTRdp[y][x] = min(minTRdp[y][x], grid[y][x+1]);
                if (y > 0) minTRdp[y][x] = min(minTRdp[y][x], grid[y-1][x]);
            }
        }
        for (int y = n - 1; y >= 0; y--) {
            for (int x = 0; x < m; x++) {
                minBLdp[y][x] = grid[y][x];
                if (x > 0) minBLdp[y][x] = min(minBLdp[y][x], grid[y][x-1]);
                if (y < n - 1) minBLdp[y][x] = min(minBLdp[y][x], grid[y+1][x]);
            }
        }
        for (int y = n - 1; y >= 0; y--) {
            for (int x = m - 1; x >= 0; x--) {
                maxBRdp[y][x] = grid[y][x];
                if (x < m - 1) maxBRdp[y][x] = max(maxBRdp[y][x], grid[y][x+1]);
                if (y < n - 1) maxBRdp[y][x] = max(maxBRdp[y][x], grid[y+1][x]);
            }
        }

        // See what will work
        int ay = -1, ax = -1;
        for (int y = 1; y < n; y++) {
            for (int x = 1; x < m; x++) {
                int tl = maxTLdp[y-1][x-1];
                int tr = minTRdp[y-1][x];
                int bl = minBLdp[y][x-1];
                int br = maxBRdp[y][x];
                if (tl < bl && tr > br) {
                    ay = y;
                    ax = x;
                }
            }
        }

        // Print the answer
        if (ay == -1) {
            cout << "NO" << endl;
        } else {
            cout << "YES" << endl;
            for (int i = 0; i < n; i++) {
                cout << (idxcopy[i] < ay ? "B" : "R");
            }
            cout << " " << ax << endl;
        }
    }

    return 0;
}