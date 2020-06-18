#include <iostream>
#include <string>
#include <cstring>
using namespace std;

#define MAXN 2010

int dp[MAXN][MAXN];

int main() {
    int t; cin >> t;
    while (t--) {
        string a, b; cin >> a >> b;
        int n = a.length(), m = b.length();
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= m; j++) {
                if (i == 0) dp[i][j] = j;
                else if (j == 0) dp[i][j] = i;
                else if (a[i-1] == b[j-1]) dp[i][j] = dp[i-1][j-1];
                else dp[i][j] = min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1])) + 1;
            }
        }
        cout << dp[n][m] << endl;
    }

    return 0;
}