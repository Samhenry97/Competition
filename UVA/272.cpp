#include <string>
#include <iostream>

using namespace std;

int main() {
	string line;
	bool cur = true;

	while(getline(cin, line)) {
		int pos = line.find("\"");
		while(pos >= 0) {
			if(cur) {
				line.replace(pos, 1, "``");
			} else {
				line.replace(pos, 1, "''");
			}
			cur = !cur;

			pos = line.find("\"", pos);
		}
		cout << line << endl;
	}

	return 0;
}