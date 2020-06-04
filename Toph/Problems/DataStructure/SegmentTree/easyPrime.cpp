#include <iostream>
using namespace std;

#define MAXN 100001

typedef long long int ll;

int seg[2*MAXN];
int a[MAXN];
int n;

ll pow(ll base, ll exp, ll mod) {
    ll res = 1;
    while (exp) {
        if (exp & 1) res = (res * base) % mod;
        base = (base * base) % mod;
        exp >>= 1;
    }
    return res;
}
 
bool witness(ll n, ll s, ll d, ll a) {
    ll x = pow(a, d, n), y;
 
    while (s) {
        y = x * x % n;
        if (y == 1 && x != 1 && x != n - 1) return false;
        x = y;
        s--;
    }
    return y == 1;
}
 
bool prime(ll n) {
    if (n < 2) return false;
    if (!(n & 1) && n != 2) return false;
    if (n % 3 == 0 && n != 3) return false;
    if (n <= 3) return true;
 
    ll d = n >> 1;
    ll s = 1;
    while (!(d & 1)) {
        d >>= 1;
        s++;
    }
 
    if (n < 1373653)
        return witness(n, s, d, 2) && witness(n, s, d, 3);
    if (n < 9080191)
        return witness(n, s, d, 31) && witness(n, s, d, 73);
    if (n < 4759123141)
        return witness(n, s, d, 2) && witness(n, s, d, 7) && witness(n, s, d, 61);
    if (n < 1122004669633)
        return witness(n, s, d, 2) && witness(n, s, d, 13) && witness(n, s, d, 23) && witness(n, s, d, 1662803);
    if (n < 2152302898747)
        return witness(n, s, d, 2) && witness(n, s, d, 3) && witness(n, s, d, 5) && witness(n, s, d, 7) && witness(n, s, d, 11);
    if (n < 3474749660383)
        return witness(n, s, d, 2) && witness(n, s, d, 3) && witness(n, s, d, 5) && witness(n, s, d, 7) && witness(n, s, d, 11) && witness(n, s, d, 13);
    return witness(n, s, d, 2) && witness(n, s, d, 3) && witness(n, s, d, 5) && witness(n, s, d, 7) && witness(n, s, d, 11) && witness(n, s, d, 13) && witness(n, s, d, 17);
}

void build() {
    for (int i = 0; i < n; i++)
        seg[n + i] = prime(a[i]);
    for (int i = n - 1; i > 0; i--)
        seg[i] = seg[i << 1] + seg[i << 1 | 1];
}

void update(int u, int v) {
    u += n;
    seg[u] = prime(v);
    for (int i = u; i > 1; i >>= 1)
        seg[i >> 1] = seg[i] + seg[i ^ 1];
}

int query(int l, int r) {
    int res = 0;
    for (l += n, r += n; l < r; l >>= 1, r >>= 1) {
        if (l & 1) res += seg[l++];
        if (r & 1) res += seg[--r];
    }
    return res;
}

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) cin >> a[i];
    build();

    int q; cin >> q;
    while(q--) {
        int t, x, y; cin >> t >> x >> y;
        if (t == 1) {
            cout << query(--x, y) << endl;
        } else {
            update(--x, y);
        }
    }

    return 0;
}