#include <bits/stdc++.h>

using namespace std;

int main() {
	int n, k; cin >> n >> k;
	vector<int> stack;
	int pos = 0;
	for(int i = 0; i < k; i++) {
		string tmp; cin >> tmp;
		if(tmp == "undo") {
			int amt; cin >> amt;
			pos = stack[stack.size() - amt - 1];
			stack.resize(stack.size() - amt);
		} else {
			int amt; istringstream(tmp) >> amt;
			pos += amt;
			while(pos < 0) { pos += n; }
			while(pos >= n) { pos -= n; }
			stack.push_back(pos);
		}
	}
	cout << pos << endl;

	return 0;
}