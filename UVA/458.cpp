#include <string>
#include <iostream>

using namespace std;

int main() {
	string line;
	int diff = '\'' - ' ';

	while(getline(cin , line)) {
		for(int i = 0; i < line.length(); i++) {
			line[i] = line[i] - diff;
		}
		cout << line << endl;
	}

	return 0;
}