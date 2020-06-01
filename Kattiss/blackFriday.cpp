#include <iostream>

using namespace std;

int main() {
	int n;
	cin >> n;

	int totals[] = {0,0,0,0,0,0};
	int pos[n];

	int temp;
	for(int i = 0; i < n; i++) {
		cin >> temp;
		totals[temp - 1]++;
		pos[i] = temp - 1;
	}

	for(int i = 5; i >= 0; i--) {
		if(totals[i] == 1) {
			for(int j = 0; j < n; j++) {
				if(pos[j] == i) {
					cout << j + 1 << endl;
					break;
				}
			}
			return 0;
		}
	}

	cout << "none" << endl;

	return 0;
}