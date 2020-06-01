#include <iostream>
#include <string>

using namespace std;

int main() {
	int n; cin >> n;

	while(n != -1) {
		string grid[n];
		for(int i = 0; i < n; i++) {
			grid[i] = "";
			int tmp; cin >> tmp;
			for(int b = n - 1; b >= 0; b--) {
				grid[i] += (tmp & (1 << b)) ? '1' : '0';
			}
		}

		int hor = 0, ver = 0, maxHor = 0, maxVer = 0;
		bool horFound = false, verFound = false;

		for(int y = 0; y < n; y++) {
			for(int x = 0; x < n; x++) {
				if(grid[y][x] == '1') {
					if(horFound) {
						hor += 1;
					} else {
						horFound = true;
						hor = 1;
					}
				} else {
					horFound = false;
					if(hor > maxHor) {
						maxHor = hor;
					}
					hor = 0;
				}
			}

			if(hor > maxHor) {
				maxHor = hor;
			}
			hor = 0;
			horFound = false;
		}

		if(hor > maxHor) {
			maxHor = hor;
		}

		for(int x = 0; x < n; x++) {
			for(int y = 0; y < n; y++) {
				if(grid[y][x] == '1') {
					if(verFound) {
						ver += 1;
					} else {
						verFound = true;
						ver = 1;
					}
				} else {
					verFound = false;
					if(ver > maxVer) {
						maxVer = ver;
					}
					ver = 0;
				}
			}

			if(ver > maxVer) {
				maxVer = ver;
			}
			ver = 0;
			verFound = false;
		}

		if(ver > maxVer) {
			maxVer = ver;
		}

		if(maxHor == maxVer) {
			cout << maxHor << " " << "both" << endl;
		} else if(maxHor > maxVer) {
			cout << maxHor << " " << "horizontal" << endl;
		} else {
			cout << maxVer << " " << "vertical" << endl;
		}

		cin >> n;
	}
}