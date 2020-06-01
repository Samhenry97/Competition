#include<bits/stdc++.h> 
using namespace std; 

#define MAXN 701

struct Edge {
    int v;
    int flow;
    int cap;
};

int n, m;
vector<Edge> adj[MAXN];
int level[MAXN];
int start[MAXN];

bool computeLevels(int s, int t) {
    fill(level, level + n, -1);
    level[s] = 0;
    queue<int> bfs({s});
    while(!bfs.empty()) {
        int u = bfs.front(); bfs.pop();
        for(int i = 0; i < adj[u].size(); i++) {
            Edge &e = adj[u][i];
            if(level[e.v] < 0 and e.flow < e.cap) {
                level[e.v] = level[u] + 1;
                bfs.push(e.v);
            }
        }
    }
    return level[t] >= 0;
}

int sendFlow(int u, int t, int flow) {
    if(u == t) return flow;
    for(; start[u] < adj[u].size(); start[u]++) {
        Edge &e = adj[u][start[u]];
        if(level[e.v] == level[u] + 1 and e.flow < e.cap) {
            int curFlow = min(flow, e.cap - e.flow);
            int tempFlow = sendFlow(e.v, t, curFlow);
            if(tempFlow > 0) {
                e.flow += tempFlow;
                return tempFlow;
            }
        }
    }
    return 0;
}

int dinic(int s, int t) {
    if(s == t) return 0;
    int total = 0;
    while(computeLevels(s, t)) {
        fill(start, start + n, 0);
        while(int flow = sendFlow(s, t, INT_MAX))
            total += flow;
    }
    return total;
}

int main() {
    ios::sync_with_stdio(false);

    unordered_map<string, int> keys;
    cin >> m;
    while(m--) {
        string u, v; int c; cin >> u >> v >> c;
        if(keys.find(u) == keys.end()) keys[u] = n++;
        if(keys.find(v) == keys.end()) keys[v] = n++;
        adj[keys[u]].push_back({keys[v], 0, c});
    }

    cout << dinic(keys["A"], keys["Z"]) << endl;

    return 0; 
} 
