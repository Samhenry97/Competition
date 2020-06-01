#include <iostream>

using namespace std;

int main() {
	int n, a, b;
	cin >> n;

	for(int i = 0; i < n; i++) {
		cin >> a >> b;
		if(a % 2 != 1) a++;
		if(b % 2 != 1) b--;
		int sum = 0;
		for(; a <= b; a += 2) {
			sum += a;
		}
		cout << "Case " << i + 1 << ": " << sum << endl;
	}

	return 0;
}