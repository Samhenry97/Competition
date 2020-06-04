#include <iostream>
#include <vector>
#include <set>
using namespace std;

#define MAXN 100001

multiset<int> seg[2*MAXN];
vector<int> adj[MAXN];
vector<int> tree[MAXN];
bool vis[MAXN];
int a[MAXN];
int idx[MAXN];
int sz[MAXN];
int cost[MAXN];
int n, q;
int id;

void build() {
    for (int i = 0; i < n; i++)
        seg[n + i].insert(a[i]);
    for (int i = n - 1; i > 0; i--) {
        seg[i].insert(seg[i << 1].begin(), seg[i << 1].end());
        seg[i].insert(seg[i << 1 | 1].begin(), seg[i << 1 | 1].end());
    }
}

void update(int u, int v) {
    u += n;
    int prev = *seg[u].begin();
    seg[u].clear();
    seg[u].insert(v);
    for (int i = u; i > 1; i >>= 1) {
        seg[i >> 1].erase(seg[i >> 1].find(prev));
        seg[i >> 1].insert(v);
    }
}

int query(int l, int r, int v) {
    int res = 0;
    for (l += n, r += n; l < r; l >>= 1, r >>= 1) {
        if (l & 1) {
            res += distance(seg[l].upper_bound(v), seg[l].end());
            l++;
        }
        if (r & 1) {
            r--;
            res += distance(seg[r].upper_bound(v), seg[r].end());
        }
    }
    return res;
}

int root(int u) {
    idx[u] = id++;
    int size = 1;
    for (auto v : adj[u]) {
        if (!vis[v]) {
            vis[v] = true;
            tree[u].push_back(v);
            size += root(v);
        }
    }
    sz[u] = size;
    return size;
}

int main() {
    cin >> n >> q;
    for (int i = 0; i < n; i++) cin >> cost[i];
    for (int i = 0; i < n - 1; i++) {
        int u, v; cin >> u >> v;
        adj[--u].push_back(--v);
        adj[v].push_back(u);
    }
    vis[0] = true;
    root(0);
    for (int i = 0; i < n; i++) a[i] = cost[idx[i]];
    build();

    while(q--) {
        int t; cin >> t;
        if (t == 1) {
            int u, v; cin >> u >> v;
            update(--u, v);
        } else {
            int u; cin >> u;
            int l = idx[--u];
            int r = l + sz[u];
            cout << query(l, r, *seg[u+n].begin()) << endl;
        }
    }

    return 0;
}