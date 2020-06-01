#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

#define MAXN 500001
#define MOD 1000000007LL

typedef long long int ll;

ll disjoint[MAXN];
ll n, m, q, k;

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

ll pow(ll base, ll exp, ll mod) {
    ll res = 1;
    while (exp) {
        if (exp & 1) res = (res * base) % mod;
        base = (base * base) % mod;
        exp >>= 1;
    }
    return res;
}

ll compute(ll size) {
    return k * pow(k-1, size-1, MOD) % MOD;
}

int main() {
    ios::sync_with_stdio(false);

    fill(disjoint, disjoint + MAXN, -1);
    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        ll u, v; cin >> u >> v; u--; v--;
        merge(u, v);
    }

    bool gt = false;
    vector<ll> sizes;
    for (int i = 0; i < n; i++) {
        if (disjoint[i] < 0) {
            if (-disjoint[i] > 1) gt = true;
            sizes.push_back(-disjoint[i]);
        }
    }

    cin >> q;
    while(q--) {
        cin >> k;
        ll ans = 0;
        if (!gt || k > 1) {
            for (auto size : sizes) {
                ans = (ans + compute(size)) % MOD;
            }
        }
        cout << ans << endl;   
    }
}