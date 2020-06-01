#include <iostream>
using namespace std;

typedef long long ll;

ll m[3];
ll mp[3];
ll ans;

int main() {
    string s; cin >> s;
    for (int i = 0; i < s.size(); i++) {
        int mod = (s[i]-'0') % 3;
        for (int j = 0; j < 3; j++)
            m[j] = mp[(3 - mod + j) % 3];
        m[mod]++;
        ans += m[0];
        for (int j = 0; j < 3; j++)
            mp[j] = m[j];
    }

    cout << ans << endl;

    return 0;
}