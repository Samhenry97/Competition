#include <iostream>
#include <vector>

using namespace std;

int main() {
	int n; cin >> n;

	while(n--) {
		int temp; cin >> temp;
		for(int i = 0; i < 256; i++) {
			char test = (char) (i ^ (i << 1));
			if(test == (char) temp) {
				cout << i << " ";
				break;
			}
		}
	}

	return 0;
}