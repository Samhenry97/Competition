#include <string>
#include <iostream>

using namespace std;

int main() {
	string correct = " 1234567890-=WERTYUIOP[]SDFGHJKL;'\\XCVBNM,./";
	string map 	   = " `1234567890-QWERTYUIOP[ASDFGHJKL;'ZXCVBNM,.";

	string line;
	while(getline(cin, line)) {
		for(int i = 0; i < line.length(); i++) {
			int pos = correct.find(string(1, line[i]));
			line[i] = map[pos];
		}
		cout << line << endl;
	}
}