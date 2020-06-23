#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <utility>
using namespace std;

int main() {
    ios::sync_with_stdio(false); cin.tie(0);

    int n, k; cin >> n >> k;
    k = k % 2 == 0 ? k / 2 : k / 2 + 1;
    vector<pair<int, int>> a;
    for (int i = 0; i < n; i++) {
        int tmp; cin >> tmp;
        a.push_back({ tmp, i });
    }
    sort(a.begin(), a.end());

    set<int> prev;
    int ans = 0;
    for (int i = 0; i < n && k; i++) {
        int idx = a[i].second;
        if (prev.find(idx) == prev.end()) {
            k--;
            ans = a[i].first;
            prev.insert(idx-1);
            prev.insert(idx+1);
        }
    }
    cout << ans << endl;

    return 0;
}