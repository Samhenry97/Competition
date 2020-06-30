#include <algorithm>
#include <iostream>
using namespace std;

#define MAXN 300001

int a[MAXN];
int disjoint[MAXN];
bool vis[MAXN];

int find(int x) {
    int par = x;
    while(disjoint[par] >= 0) par = disjoint[par];
    if (par != x) disjoint[x] = par;
    return par;
}

void merge(int x, int y) {
    int parx = find(x);
    int pary = find(y);

    if (parx == pary) return;
    if (disjoint[parx] < disjoint[pary]) {
        disjoint[pary] += disjoint[parx];
        disjoint[parx] = pary;
    } else {
        disjoint[parx] += disjoint[pary];
        disjoint[pary] = parx;
    }
}

int main() {
    ios::sync_with_stdio(false); cin.tie(0);

    fill(disjoint, disjoint + MAXN, -1);
    int n; cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> a[i]; a[i]--;
        if (i != a[i]) merge(i, a[i]);
    }
    int cyc = 0;
    for (int i = 0; i < n; i++) {
        int par = find(i);
        if (!vis[par]) {
            while (a[par] != par && !vis[par]) {
                vis[par] = true;
                par = a[par];
            }
            cyc += vis[par];
        }
    }
    int conn = count_if(disjoint, disjoint + n, [](int x) { return x < 0; });
    cout << conn + (cyc == conn ? 0 : -1) << endl;

    return 0;
}