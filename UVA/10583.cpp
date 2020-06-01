#include "bits/stdc++.h"

using namespace std;

int disjoint[50001];

int find(int x) {
    int par = x;
    while(disjoint[par] >= 0) { par = disjoint[par]; }
    if(par != x) { disjoint[x] = par; }
    return par;
}

void merge(int x, int y) {
    int parx = find(x), pary = find(y);

    if(parx == pary) { return; }
    if(disjoint[parx] < disjoint[pary]) {
        disjoint[pary] += disjoint[parx];
        disjoint[parx] = pary;
    } else {
        disjoint[parx] += disjoint[pary];
        disjoint[pary] = parx;
    }
}

int main() {
    ios::sync_with_stdio(false);
    int n, m; 
    int c = 1;

    while(scanf("%d%d", &n, &m) == 2 && (n or m)) {
        fill(disjoint, disjoint + n, -1);
        while(m--) {
            int i, j; scanf("%d%d", &i, &j);
            merge(--i, --j);
        }

        int total = 0;
        for(int i = 0; i < n; i++) {
            if(disjoint[i] < 0) { total++; }
        }

        printf("Case %d: %d\n", c, total);
        c++;
    }

    return 0;
}