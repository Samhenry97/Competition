#include <iostream>
#include <vector>
#include <queue>
#include <utility>
#include <set>
#include <algorithm>
using namespace std;

#define MAXN 500001

vector<int> adj[MAXN];
pair<int, int> goals[MAXN];
int goal[MAXN];
set<int> neigh[MAXN];
int top[MAXN];

int main() {
    int n, m; cin >> n >> m;
    for (int i = 0; i < m; i++) {
        int u, v; cin >> u >> v;
        adj[--u].push_back(--v);
        adj[v].push_back(u);
    }
    for (int i = 0; i < n; i++) {
        cin >> goal[i];
        goals[i] = { goal[i], i };
    }

    bool valid = true;
    for (int u = 0; u < n && valid; u++) {
        int gu = goal[u];
        for (auto v : adj[u]) {
            int gv = goal[v];
            if (gu == gv) valid = false;
            if (gu > gv) neigh[u].insert(gv);
            if (gv > gu) neigh[v].insert(gu);
        }
    }

    for (int i = 0; i < n && valid; i++) {
        for (int j = 1; j < goal[i]; j++) {
            if (neigh[i].find(j) == neigh[i].end()) {
                valid = false;
                break;
            }
        }
    }

    if (!valid) {
        cout << -1 << endl;
    } else {
        sort(goals, goals + n);
        for (int i = 0; i < n; i++) {
            cout << goals[i].second + 1 << " ";
        }
        cout << endl;
    }

    return 0;
}