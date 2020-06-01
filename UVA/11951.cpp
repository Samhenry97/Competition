#include <bits/stdc++.h>
using namespace std;

struct Size {
    int w, h;
    Size(int iw, int ih) : w(iw), h(ih) { ; }
    bool operator<(const Size &other) const {
        return ((w + 1) * (h + 1)) > ((other.w + 1) * (other.h + 1));
    }
};

int main() {
    int t; scanf("%d", &t);

    for(int j = 0; j < t; j++) {
        int n, m, k; scanf("%d%d%d", &n, &m, &k);
        vector<vector<int>> dp(n, vector<int>(m, 0));
        
        for(int y = 0; y < n; y++) {
            for(int x = 0; x < m; x++) {
                int tmp; scanf("%d", &tmp);
                dp[y][x] += tmp;
                if(x > 0) { dp[y][x] += dp[y][x - 1]; }
                if(y > 0) { dp[y][x] += dp[y - 1][x]; }
                if(x > 0 && y > 0) { dp[y][x] -= dp[y - 1][x - 1]; }
            }
        }
        
        vector<Size> sizes;
        int mi = min(n, m);
        int ma = max(n, m);
        for(int y = mi - 1; y >= 0; y--) {
            for(int x = ma; x >= y; x--) {
                sizes.push_back(Size(x, y));
            }
        }
        sort(sizes.begin(), sizes.end());
        
        int maxArea = -1;
        int cheapest = 0x7FFFFFFF;
        for(int i = 0; i < sizes.size() && maxArea == -1; i++) {
            int sn = sizes[i].w, sm = sizes[i].h;
            
            if(sn < n && sm < m) {
                for(int y = 0; y < n - sn; y++) {
                    for(int x = 0; x < m - sm; x++) {
                        int y2 = y + sn;
                        int x2 = x + sm;
                        int total = dp[y2][x2];
                        if(x > 0) { total -= dp[y2][x - 1]; }
                        if(y > 0) { total -= dp[y - 1][x2]; }
                        if(x > 0 && y > 0) { total += dp[y - 1][x - 1]; }
                        if(total <= k) {
                            maxArea = (y2 - y + 1) * (x2 - x + 1);
                            if(total < cheapest) { cheapest = total; }
                        }
                    }
                }
            }
            
            swap(sn, sm);
            if(sn < n && sm < m) {
                for(int y = 0; y < n - sn; y++) {
                    for(int x = 0; x < m - sm; x++) {
                        int y2 = y + sn;
                        int x2 = x + sm;
                        int total = dp[y2][x2];
                        if(x > 0) { total -= dp[y2][x - 1]; }
                        if(y > 0) { total -= dp[y - 1][x2]; }
                        if(x > 0 && y > 0) { total += dp[y - 1][x - 1]; }
                        if(total <= k) {
                            maxArea = (y2 - y + 1) * (x2 - x + 1);
                            if(total < cheapest) { cheapest = total; }
                        }
                    }
                }
            }
        }

        printf("Case #%d: %d %d\n", j + 1, maxArea == -1 ? 0 : maxArea, maxArea == -1 ? 0 : cheapest);
    }
    
    return 0;
}