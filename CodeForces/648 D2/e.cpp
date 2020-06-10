#include <iostream>
using namespace std;

#define MAXN 505

typedef long long int ll;

ll a[MAXN];

int main() {
    ios::sync_with_stdio(false);
    int n; cin >> n;
    for (int i = 0; i < n; i++) cin >> a[i];
    ll ans = 0;
    for (int i = 0; i < n; i++)
        for (int j = i; j < n; j++)
            for (int k = j; k < n; k++)
                ans = max(ans, a[i] | a[j] | a[k]);
    cout << ans << endl;

    return 0;
}