#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
    
using namespace std;
    
#define MAXN 8001
    
int a[MAXN];
int pre[MAXN];
bool spec[MAXN];
int found[MAXN];
    
int main() {
    ios::sync_with_stdio(false);
    int t; cin >> t;
    while(t--) {
        int n; cin >> n;
        fill(spec, spec + n, false);
        fill(found, found + n, 0);
        for (int i = 0; i < n; i++) {
            cin >> a[i];
            found[a[i]-1]++;
        }
    
        pre[0] = a[0];
        for (int i = 1; i < n; i++) pre[i] = a[i] + pre[i-1];
    
        for (int i = 0; i < n; i++) {
            int sum = 0;
            for (int j = i+1; j < n && sum <= n; j++) {
                if (i > 0) {
                    sum = pre[j] - pre[i-1];
                } else {
                    sum = pre[j];
                }
                if (sum <= n && !spec[sum-1]) {
                    spec[sum-1] = true;
                }
            }
        }
    
        int ans = 0;
        for (int i = 0; i < n; i++) ans += spec[i] ? found[i] : 0;
        cout << ans << endl;
    }
    
    return 0;
}