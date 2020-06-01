#include <iostream>
#include <vector>

using namespace std;

int main() {
	int n;
	cin >> n;

	vector<int> data(n);
	vector<int> mins(n);
	vector<int> maxs(n);

	for(int i = 0; i < n; i++) {
		cin >> data[i];
	}

	maxs[0] = data[0];
	for(int i = 1; i < n; i++) {
		if(data[i] > maxs[i-1]) {
			maxs[i] = data[i];
		} else {
			maxs[i] = maxs[i-1];
		}
	}

	mins[n-1] = data[n-1];
	for(int i = n-2; i >= 0; i--) {
		if(data[i] < mins[i+1]) {
			mins[i] = data[i];
		} else {
			mins[i] = mins[i+1];
		}
	}

	for(int i = 0; i < maxs.size(); i++) {
		cout << maxs[i] << " ";
	}
	cout << endl;
	for(int i = 0; i < mins.size(); i++) {
		cout << mins[i] << " ";
	}
	cout << endl;

	int total = 0;
	for(int i = 1; i < n - 1; i++) {
		if(maxs[i - 1] < data[i] && data[i] < mins[i + 1]) {
			total++;
		}
	}

	cout << total << endl;

	return 0;
}