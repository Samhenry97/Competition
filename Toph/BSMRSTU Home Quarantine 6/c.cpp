#include <iostream>
#include <map>
#include <algorithm>
#include <vector>
using namespace std;

map<int, vector<int>> loc;

int main() {
    int n, q; cin >> n >> q;
    for (int i = 0; i < n; i++) {
        int tmp; cin >> tmp;
        loc[tmp].push_back(i);
    }

    while(q--) {
        int l, r, tmp; cin >> l >> r >> tmp; l--; r--;
        if (loc.find(tmp) == loc.end()) {
            cout << "NO" << endl;
            continue;
        }

        vector<int> &pos = loc[tmp];
        int lb = *lower_bound(pos.begin(), pos.end(), l);
        int rb = *lower_bound(pos.begin(), pos.end(), r);

        if ((l <= lb && lb <= r) || (l <= rb && rb <= r)) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }

    return 0;
}