#include <iostream>
#include <vector>
#include <queue>
#include <string>

using namespace std;

int main() {
	int c;
	cin >> c;

	while(c--) {
		queue<int> left;
		queue<int> right;

		int l, m;
		cin >> l >> m;
		l *= 100;

		int length;
		string side;
		for(int i = 0; i < m; i++) {
			cin >> length >> side;
			if(side == "left") {
				left.push(length);
			} else {
				right.push(length);
			}
		}

		int passes = 1;
		side = "l";
		while(!left.empty() || !right.empty()) {
			int total = 0;
			int cur = 0;
			bool empty = false;
			if(side == "l" && !left.empty()) {
				while(total <= l) {
					cur = left.front(); left.pop();
					total += cur;
					if(left.empty() && total > l) { empty = true; break; }
				}
				if(empty) { left.push(cur); }
				side = "r";
			} else {
				while(total <= l && !right.empty()) {
					cur = right.front(); right.pop();
					total += cur;
					if(right.empty() && total > l) { empty = true; break; }
				}
				if(empty) { right.push(cur); }
				side = "l";
			}		
			passes++;
		}

		cout << passes << endl;
	}

	return 0;
}