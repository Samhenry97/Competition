#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	int t; cin >> t;

	while(t--) {
		map<char, double> cost;

		int chars; cin >> chars;
		while(chars--) {
			char c; double v; cin >> c >> v;
			cost[c] = v;
		}

		int lines; cin >> lines;
		double total = 0;
		cin.ignore(); cin.ignore();
		while(lines--) {
			string tmp; getline(cin, tmp);
			for(auto c : tmp) {
				if(cost.find(c) != cost.end()) {
					total += cost[c];
				}
			}
		}

		printf("%0.2lf$\n", total / 100.0);
	}

	return 0;
}