#include <iostream>

using namespace std;

int main() {
	int q; cin >> q;

	while(q--) {
		int n; cin >> n;
		bool valid = n & 1;

		if(!valid) {
			for(int i = 0; i < n; i++) {
				int tmp; cin >> tmp;
			}
		} else {
			for(int i = 0; i < n / 2 + 1; i++) {
				int tmp; cin >> tmp;
				if(tmp != i + 1) { valid = false; }
			}

			for(int i = 0; i < n / 2; i++) {
				int tmp; cin >> tmp;
				if(tmp != (n / 2) - i) { valid = false; }
			}
		}

		cout << (valid ? "yes" : "no") << endl;
	}

	return 0;
}