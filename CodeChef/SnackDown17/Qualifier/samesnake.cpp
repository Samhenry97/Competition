#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	long long t; cin >> t;

	while(t--) {
		long long x11, y11, x12, y12, x21, y21, x22, y22;
		cin >> x11 >> y11 >> x12 >> y12 >> x21 >> y21 >> x22 >> y22;

		if(y11 > y12) { swap(y11, y12); }
		if(y21 > y22) { swap(y21, y22); }
		if(x11 > x12) { swap(x11, x12); }
		if(x21 > x22) { swap(x21, x22); }

		bool valid = false;
		bool vertical1 = x11 == x12;
		bool vertical2 = x21 == x22;

		if(x11 == x12 && y11 == y12) {
			vertical1 = vertical2;
		} else if(x21 == x22 && y21 == y22) {
			vertical2 = vertical1;
		} 

		if(vertical1 != vertical2) { //perpendicular
			valid = (x11 == x21 && y11 == y21) || (x11 == x22 && y11 == y22) || (x12 == x21 && y12 == y21) || (x12 == x22 && y12 == y22);
		} else { // parallel
			if(vertical1) {
				valid = (x11 == x21) && !(y12 < y21 || y11 > y22);
			} else {
				valid = (y11 == y21) && !(x12 < x21 || x11 > x22);
			}
		}

		cout << (valid ? "yes" : "no") << endl;
	}

	return 0;
}