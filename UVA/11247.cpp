#include <iostream>

using namespace std;

int main() {
	int m, x;

	while(cin >> m >> x) {
		if(m == 0 && x == 0) { break; }

		if(100 - x != 0) {
			cout << (int) (m * 100 / (100 - x)) - 1 << endl;
		} else {
			cout << 0 << endl;
		}
		
	}

	return 0;
}