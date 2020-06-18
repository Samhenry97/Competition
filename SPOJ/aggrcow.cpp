#include <bits/stdc++.h>
using namespace std;
    
int n, c, ans, pos[100001];
    
bool valid(int space) {
    int cows = 1, idx = pos[0];
    for(int i = 0; i < n; i++) {
        if(pos[i] - idx >= space) {
            if(++cows == c) { ans = max(ans, space); return true; }
            idx = pos[i];
        }
    }
    return false;
}
    
int main() {
    ios::sync_with_stdio(false);
    int t; cin >> t;
    
    while(t--) {
        cin >> n >> c; ans = 0;
        for(int i = 0; i < n; i++) { cin >> pos[i]; }
        sort(pos, pos + n);
    
        int bot = 0, top = pos[n - 1] - pos[0] + 1, mid = (bot + top) >> 1;
        while(bot < top - 1) {
            if(valid(mid)) {
                bot = mid;
            } else {
                top = mid;
            }
            mid = (bot + top) >> 1;
        }
    
        cout << ans << endl;
    }
    
    return 0;
} 