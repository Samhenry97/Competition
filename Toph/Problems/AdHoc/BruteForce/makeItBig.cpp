#include <string>
#include <sstream>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cassert>
using namespace std;

typedef long long int ll;

int main() {
    int t; cin >> t;
    while(t--) {
        ll tmp; cin >> tmp;
        string s = to_string(tmp);
        int n = s.size();
        ll ans = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                swap(s[i], s[j]);
                for (int x = 0; x < n; x++) {
                    for (int y = x + 1; y < n; y++) {
                        swap(s[x], s[y]);
                        ans = max(ans, stoll(s));
                        swap(s[x], s[y]);
                    }
                }
                swap(s[i], s[j]);
            }
        }
        cout << ans << endl;
    }
    return 0;
}