#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
    
#define MAXN 100001
int gran[MAXN];
    
int main() {
    int t; cin >> t;
    while(t--) {
        int n; cin >> n;
        int ans = 1;
        for (int i = 0; i < n; i++) cin >> gran[i];
        sort(gran, gran + n);
        for (int i = 0; i < n; i++) {
            if (gran[i] - i <= 1) ans = i + 2;
        }
        cout << ans << endl;
    }
    
    return 0;
}