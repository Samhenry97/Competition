#include <iostream>
#include <numeric>
#include <climits>
#include <vector>
using namespace std;

typedef long long int ll;

ll a[200001];

int main() {
    ios::sync_with_stdio(false); cin.tie(0);
    int t; cin >> t;
    while(t--) {
        int n; cin >> n;
        for (int i = 0; i < n; i++) cin >> a[i];
        vector<pair<int, int>> pos;
        int start = 0;
        ll maxSoFar = -LLONG_MAX, maxEndingHere = 0;
        for (int i = 0; i < n / 2; i++) {
            int cur = a[i*2+1] - a[i*2];
            maxEndingHere += cur;
            if (maxSoFar < maxEndingHere) {
                maxSoFar = maxEndingHere;
                pos.clear();
                pos.push_back({ start, i });
            } else if(maxSoFar == maxEndingHere) {
                pos.push_back({ start, i });
            } else if(maxEndingHere < 0) {
                maxEndingHere = 0;
                start = i + 1;
            }
        }
        cout << "FOR: " << t << endl;
        for (int i = 0; i < pos.size(); i++) {
            cout << pos[i].first << " " << pos[i].second << endl;
        }
    }

    return 0;
}