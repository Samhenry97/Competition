#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main() {
	int n, d;
	cin >> n >> d;

	vector<int> data[d];

	int temp;
	for(int i = 0; i < n; i++) {
		cin >> temp;
		data[temp % d].push_back(temp);
	}

	int total = 0;
	for(int i = 0; i < d; i++) {
		if(data[i].size() > 2) {
			for(int j = 0; j < data[i].size() - 2; j++) {
				if((data[i][j+2] - data[i][j+1] == d) && (data[i][j+1] - data[i][j] == d)) {
					total++;
				}
			}
		}
	}

	cout << total << endl;

	return 0;
}