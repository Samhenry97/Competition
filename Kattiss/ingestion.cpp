#include <bits/stdc++.h>
using namespace std;

int n, c;
int cals[101];
int dp[101][20001];
int maxCals = -1;

int sum(vector<int> &consumed) {
	int sum = 0;
	for(int i = 0; i < consumed.size(); i++) {
		sum += consumed[i];
	}
	return sum;
}

void calc(vector<int> &consumed, int idx, int cur) {
	if(idx == n) {
		maxCals = max(maxCals, sum(consumed));
		return;
	}

	int back = consumed.size() - 1;
	if(consumed.size() >= 2 && consumed[back] + consumed[back-1] == 0) {
		consumed.push_back(min(cals[idx], c));
		calc(consumed, idx + 1, c);
		consumed.pop_back();
	} else {
		consumed.push_back(min(cals[idx], cur));
		calc(consumed, idx + 1, (int) ((float) cur * (2.0 / 3.0)));
		consumed.pop_back();

		consumed.push_back(0);
		calc(consumed, idx + 1, cur);
		consumed.pop_back();
	}
}

int main() {
	ios::sync_with_stdio(false);
	scanf("%d%d", &n, &c);
	for(int i = 0; i < n; i++) { scanf("%d", cals + i); }

	vector<int> cals;
	calc(cals, 0, c);
	printf("%d\n", maxCals);

	return 0;
}