#include <iostream>

using namespace std;

int largestSquare(long n) {
	int lastSquare = 0;
	for(int i = 0; i < 1000000; i++) {
		if(i * i >= n) {
			return lastSquare + 1;
		} else {
			lastSquare = i;
		}
	}
}

int main() {
	long n;
	cin >> n;
	while(n != 0) {
		int c = largestSquare(n);
		int amt = c * 2 - 1;
		int mid = (c-1) * (c-1) + amt / 2 + 1;
		if(n == mid) {
			cout << c << " " << c << endl;
		} else if(c & 0x1) { //Odd
			if(n < mid) {
				cout << c << " " << c - (mid - n) << endl;
			} else {
				cout << c - (n - mid) << " " << c << endl;
			}
		} else {			//Even
			if(n < mid) {
				cout << c - (mid - n) << " " << c << endl;
			} else {
				cout << c << " " << c - (n - mid) << endl;
			}
		}

		cin >> n;
	}

	return 0;
}