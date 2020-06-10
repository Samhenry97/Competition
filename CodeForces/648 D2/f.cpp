#include <set>
#include <iostream>
#include <algorithm>
using namespace std;

#define MAXN 501

int t, n;
int a[MAXN];
int b[MAXN];
int sa[MAXN];
int sb[MAXN];
pair<int, int> pa[MAXN/2];
pair<int, int> pb[MAXN/2];

int main() {
    ios::sync_with_stdio(false);
    cin >> t;
    while(t--) {
        cin >> n;
        bool valid = true;
        for (int i = 0; i < n; i++) {
            cin >> a[i];
            sa[i] = a[i];
        }
        for (int i = 0; i < n; i++) {
            cin >> b[i];
            sb[i] = b[i];
        }

        // Multiset different
        sort(sa, sa + n);
        sort(sb, sb + n);
        for (int i = 0; i < n; i++)
            if (sa[i] != sb[i]) valid = false;

        // Middle element different
        if (n % 2 == 1 && a[n/2] != b[n/2]) valid = false;

        for (int i = 0; i*2 < n; i++) {
            int x = a[i], y = a[n-i-1];
            pa[i] = { min(x, y), max(x, y) };
            x = b[i]; y = b[n-i-1];
            pb[i] = { min(x, y), max(x, y) };
        }

        sort(pa, pa + n/2);
        sort(pb, pb + n/2);
        
        for (int i = 0; i*2 < n; i++)
            if (pa[i] != pb[i]) valid = false;

        cout << (valid ? "Yes" : "No") << endl;
    }

    return 0;
}
