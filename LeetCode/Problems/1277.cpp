#define MAXN 300

class Solution {
public:
    int countSquares(vector<vector<int>>& grid) {
        int n = max(grid.size(), grid[0].size());
        vector<vector<int>> dp(grid.size(), vector<int>(grid[0].size(), 0));
        int ans = 0;
        for (int y = 0; y < grid.size(); y++) {
            for (int x = 0; x < grid[y].size(); x++) {
                dp[y][x] = grid[y][x];
                if (x) dp[y][x] += dp[y][x-1];
                if (y) dp[y][x] += dp[y-1][x];
                if (x && y) dp[y][x] -= dp[y-1][x-1];
                
                for (int i = 0; i <= n; i++) {
                    int yy = y - i, xx = x - i;
                    if (yy >= 0 && xx >= 0) {
                        int cnt = dp[y][x];
                        if (xx) cnt -= dp[y][xx-1];
                        if (yy) cnt -= dp[yy-1][x];
                        if (yy && xx) cnt += dp[yy-1][xx-1];
                        if (cnt == (i+1)*(i+1)) ans++;
                    } else {
                        break;
                    }
                }
            }
        }
        return ans;
    }
};