#include <bits/stdc++.h>
using namespace std;

#define MAXN 35
int dp[MAXN][MAXN];

int main() {
	ios::sync_with_stdio(false);

	int t; cin >> t;
	while(t--) {
		int n, m, k; cin >> n >> m >> k;
		for(int y = 0; y < n; y++) {
			string s; cin >> s;
			for(int x = 0; x < m; x++) {
				dp[y][x] += s[x] == 'C';
				dp[y][x] += y > 0 ? dp[y-1][x] : 0;
				dp[y][x] += x > 0 ? dp[y][x-1] : 0;
				dp[y][x] -= y > 0 and x > 0 ? dp[y-1][x-1] : 0;
			}
		}

		int minArea = 1 << 30;
		for(int h = 0; h < n; h++)
			for(int w = 0; w < m; w++)
				for(int y = 0; y < n - h; y++)
					for(int x = 0; x < m - w; x++) {
						int chips = dp[y + h][x + w];
						chips -= y > 0 ? dp[y - 1][x + w] : 0;
						chips -= x > 0 ? dp[y + h][x - 1] : 0;
						chips += y > 0 and x > 0 ? dp[y - 1][x - 1] : 0;
						minArea = chips == k ? min((h+1) * (w+1), minArea) : minArea;
					}

		cout << (minArea == (1 << 30) ? -1 : minArea) << endl;
	}

	return 0;
}