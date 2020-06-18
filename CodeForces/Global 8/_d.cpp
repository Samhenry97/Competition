#include <iostream>
#include <algorithm>
using namespace std;

typedef long long int ll;

ll a[200001];

int main() {
    ios::sync_with_stdio(false);

    ll n; cin >> n;
    ll sor = 0;
    ll sand = 1048575;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        sor |= a[i];
    }
    ll ans = 0;
    sort(a, a + n);
    for (int i = n - 1; i >= 0; i--) {
        ll tmp = (i % 2 == 0 ? a[i] | sor : a[i] & sor);
        ans += tmp * tmp;
    }
    cout << ans << endl;

    return 0;
}