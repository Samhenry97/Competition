#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

struct Point {
	int x, y;
	Point(int ix, int iy) : x(ix), y(iy) { ; }
	bool intersects(const Point &other) {
		if(x == other.x || y == other.y) { return true; }
		if(abs(x - other.x) == abs(y - other.y)) { return true; }
		return false;
	}
};

int main() {
	vector<Point> queens;

	char cur;
	for(int y = 0; y < 8; y++) {
		for(int x = 0; x < 8; x++) {
			cin >> cur;
			if(cur == '*') { queens.push_back(Point(x, y)); }
		}
	}

	bool valid = true;
	if(queens.size() != 8) valid = false;
	for(int i = 0; i < queens.size() && valid; i++) {
		for(int check = i + 1; check < queens.size(); check++) {
			if(queens[check].intersects(queens[i])) {
				valid = false;
				break;
			}
		}
	}

	cout << (valid ? "valid" : "invalid") << endl;

	return 0;
}