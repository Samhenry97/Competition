#include <bits/stdc++.h>
using namespace std;

#define MAXN 100010
#define MAXL 20
#define level 20
#define DEBUG false

int n, m, ans;

vector<int> tree[MAXN];  
int depth[MAXN], parent[MAXN][MAXL], ks[MAXN];

void dfs(int cur, int prev) {
    depth[cur] = depth[prev] + 1; 
    parent[cur][0] = prev; 
    for (int i=0; i<tree[cur].size(); i++) {
        if (tree[cur][i] != prev) 
            dfs(tree[cur][i], cur); 
    } 
} 

void preprocess() { 
    for (int i=1; i<level; i++) { 
        for (int node = 1; node <= n; node++) { 
            if (parent[node][i-1] != -1) 
                parent[node][i] = 
                    parent[parent[node][i-1]][i-1]; 
        } 
    } 
} 

int lca(int u, int v) { 
    if (depth[v] < depth[u]) 
        swap(u, v); 
  
    int diff = depth[v] - depth[u]; 
  
    for (int i=0; i<level; i++) 
        if ((diff>>i)&1) 
            v = parent[v][i]; 
  
    if (u == v) 
        return u; 
  
    for (int i=level-1; i>=0; i--) 
        if (parent[u][i] != parent[v][i]) 
        { 
            u = parent[u][i]; 
            v = parent[v][i]; 
        } 
  
    return parent[u][0]; 
}

void root(int u) {
    for(int v : tree[u]) {
        tree[v].erase(find(tree[v].begin(), tree[v].end(), u));
        root(v);
    }
}

void final(int u) {
    for(int v : tree[u]) {
        final(v);
        ks[u] += ks[v];
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin >> n >> m;
    
    for(int i = 0; i < n - 1; i++) {
        int u, v; cin >> u >> v;
        tree[++u].push_back(++v);
        tree[v].push_back(u);
    }
    
    root(1);
    dfs(1, 0);
    preprocess();

    while(m--) {
        int u, v, k; cin >> u >> v >> k;
        int par = lca(++u, ++v);
        ks[u] += k;
        ks[v] += k;
        ks[par] -= k;
        ks[parent[par][0]] -= k;
    }

    final(1);

    cout << *max_element(ks + 1, ks + n + 1) << endl;
    
    return 0;
}