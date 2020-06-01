#include <iostream>
#include <algorithm>
using namespace std;

typedef long long int ll;

#define MAXN 500001

ll teams[MAXN];
ll pref[MAXN];
ll n, x, k, cut;

bool works(int mid) {
    ll goal = (cut - mid + 1) * x;
    ll cur = pref[cut] - (mid > 0 ? pref[mid-1] : 0);
    return goal - cur <= k;
}

int main() {
    ios::sync_with_stdio(false);

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> teams[i];
    }

    sort(teams, teams + n);
    pref[0] = teams[0];
    for (int i = 1; i < n; i++) {
        pref[i] = pref[i-1] + teams[i];
    }

    int q; cin >> q;
    while(q--) {
        cin >> x >> k;
        int top = lower_bound(teams, teams + n, x) - teams;
        int ans = n - top;
        top--;
        cut = top;
        int bot = 0;
        while(top - bot > 0) {
            int mid = (bot + top) / 2;
            if (works(mid)) {
                top = mid;
            } else {
                bot = mid + 1;
            }
        }
        ans += cut - bot + works(bot);
        cout << ans << endl;
    }

    return 0;
}