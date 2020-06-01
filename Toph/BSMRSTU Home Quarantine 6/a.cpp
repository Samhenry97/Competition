#include <iostream>
#include <map>
using namespace std;

#define MAXN 100001

map<int, int> freq;

int main() {
    int n, m, k; cin >> n >> m >> k;

    for (int i = 0; i < n; i++) {
        int tmp; cin >> tmp;
        freq[tmp % k]++;
    }

    int ans = 0;
    for (int i = 0; i < m; i++) {
        int tmp; cin >> tmp;
        tmp = (k-(tmp%k))%k;
        ans += freq[tmp] > 0;
        freq[tmp]--;
    }

    cout << ans << endl;

    return 0;
}

