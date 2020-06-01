#include <iostream>
#include <string>

using namespace std;

int main() {
	int n; cin >> n;

	while(n--) {
		char c; cin >> c;

		int t; cin >> t;
		int nums[t];
		int ans[t];
		for(int i = 0; i < t; i++) {
			cin >> nums[i];
		}

		if(c == '+') {
			ans[0] = 0;
			ans[1] = nums[0];
			bool found = false;

			while(ans[0] <= nums[0]) {
				for(int i = 1; i < t - 1; i++) {
					ans[i + 1] = nums[i] - ans[i];
				}

				bool neg = false;
				for(int i = 0; i < t; i++) {
					if(ans[i] < 0) {
						neg = true;
					}
				}

				if(!neg && ans[t - 1] + ans[0] == nums[t - 1]) {
					found = true;
					for(int i = 0; i < t; i++) {
						cout << ans[i] << " ";
					}
					cout << endl;
					break;
				} else {
					ans[0] += 1;
					ans[1] = nums[0] - ans[0];
				}
			}

			if(!found) {
				cout << "no solution" << endl;
			}
		} else {
			ans[0] = 1;
			ans[1] = nums[0];
			bool found = false;

			while(ans[0] <= nums[0]) {
				for(int i = 1; i < t - 1; i++) {
					ans[i + 1] = nums[i] / ans[i];
				}

				bool neg = false;
				for(int i = 0; i < t; i++) {
					if(ans[i] < 0) {
						neg = true;
					}
				}

				if(!neg && ans[t - 1] * ans[0] == nums[t - 1]) {
					found = true;
					for(int i = 0; i < t; i++) {
						cout << ans[i] << " ";
					}
					cout << endl;
					break;
				} else {
					bool hehe = false;
					while(ans[0] <= nums[0]) {
						ans[0] += 1;
						if(nums[0] % ans[0] == 0) {
							hehe = true;
							ans[1] = nums[0] / ans[0];
						}
					}
					if(!hehe) {
						break;
					}
				}
			}

			if(!found) {
				cout << "no solution" << endl;
			}
		}
	}

	return 0;
}