#include <iostream>
#include <string>

using namespace std;

int main() {
	int r; cin >> r;

	while(r--) {
		int l; cin >> l;
		string snake; cin >> snake;

		bool valid = true;
		int state = 0;
		for(char c : snake) {
			if(c == 'H') {
				if(state == 1) {
					valid = false;
					break;
				}
				state = 1;
			} else if(c == 'T') {
				if(state == 0) {
					valid = false;
					break;
				}
				state = 0;
			}
		}

		if(state == 1 || !valid) {
			cout << "Invalid" << endl;
		} else {
			cout << "Valid" << endl;
		}
	}

	return 0;
}