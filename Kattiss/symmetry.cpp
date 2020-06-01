#include <iostream>
#include <vector>

using namespace std;

int main() {
	int n;
	int cur = 1;

	while(cin >> n) {
		if(!n) break;

		vector<string> first;
		vector<string> second;
		string temp;

		for(int i = 0; i < n; i++) {
			cin >> temp;
			if(i & 1) { //Odd
				second.push_back(temp);
			} else {
				first.push_back(temp);
			}
		}

		cout << "SET " << cur << endl;

		for(int i = 0; i < first.size(); i++) {
			cout << first[i] << endl;
		}

		for(int i = second.size() - 1; i >= 0; i--) {
			cout << second[i] << endl;
		}

		cur++;
	}

	return 0;
}