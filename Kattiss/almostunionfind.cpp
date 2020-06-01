#include <bits/stdc++.h>
using namespace std;

#define MAXN 100001
typedef long long int ll;

int n, m;
set<int> dp[MAXN];
ll sums[MAXN];
int loc[MAXN];

void merge() {
	int a, b; cin >> a >> b; a--; b--;
	if(loc[a] == loc[b]) return;
	set<int> &sa = dp[loc[a]];
	set<int> &sb = dp[loc[b]];
	if(sa.size() > sb.size()) {
		sums[loc[b]] = 0;
		for(auto el : sb) {
			sa.insert(el);
			loc[el] = loc[a];
			sums[loc[a]] += el;
		}
		sb.clear();
	} else {
		sums[loc[a]] = 0;
		for(auto el : sa) {
			sb.insert(el);
			loc[el] = loc[b];
			sums[loc[b]] += el;
		}
		sa.clear();
	}
}

void move() {
	int a, b; cin >> a >> b; a--; b--;
	if(loc[a] == loc[b]) return;
	dp[loc[a]].erase(a);
	sums[loc[a]] -= a;
	dp[loc[b]].insert(a);
	sums[loc[b]] += a;
	loc[a] = loc[b];
}

void print() {
	int a; cin >> a; a--;
	set<int> &sa = dp[loc[a]];
	cout << sa.size() << " " << sums[loc[a]] + sa.size() << endl;
}

int main() {
	ios::sync_with_stdio(false);
	while(cin >> n >> m) {
		for(int i = 0; i < n; i++) {
			loc[i] = i;
			sums[i] = i;
			dp[i].clear();
			dp[i].insert(i);
		}

		while(m--) {
			int c; cin >> c;
			switch(c) {
				case 1: merge(); break;
				case 2: move(); break;
				case 3: print(); break;
			}
		}
	}
}