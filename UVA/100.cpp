#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	int a, b;
	while(cin >> a >> b) {
		int max = 0;
		cout << a << " " << b << " ";
		if(a > b) { swap(a, b); }
		for(; a <= b; a++) {
			int count = 0;
			int i = a;
			while(i != 1) {
				if((i & 0x1)) {
					i = 3 * i + 1;
				} else {
					i = i / 2;
				}
				count++;
			}
			count++;
			if(count > max) { max = count; }
		}
		cout << max << endl;
	}
	
	return 0;
}