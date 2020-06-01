#include <iostream>
#include <string>

using namespace std;

int main() {
	string line;
	cin >> line;

	if(line.length() & 1) {
		cout << "impossible" << endl;
	}

	int i;
	int totalStart = 0;
	for(i = 0; i < line.length(); i++) {
		if(line[i] == '(') {
			totalStart++;
		} else if(totalStart == 0) {
			int totalWrong = 1;
			int startIndex = i;
			i++;
			while(totalWrong != 0 && i < line.length()) {
				if(line[i] == ')' && (i - startIndex) % 2 != 0) {
					i++;
					break;
				} else if(line[i] == ')' && (i - startIndex) % 2 == 0) {
					totalWrong++;
				} else if(line[i] == '(' && (i - startIndex) % 2 != 0) {
					totalWrong--;
				} else if(line[i] == '(' && (i - startIndex) % 2 == 0) {
					i++; 
					break;
				}
				i++;
			}
			if(totalWrong != 0 && i == line.length()) {
				cout << totalWrong << " " << totalStart << endl;
				if(totalWrong == totalStart) {
					cout << "possible" << endl;
					return 0;
				} else {
					cout << "impossible" << endl;
					return 0;
				}
			} else if(totalWrong != 0) {
				cout << "impossible" << endl;
				return 0;
			} else {
				break;
			}
		} else {
			totalStart--;
		}
	}

	for(; i < line.length(); i++) {
		if(line[i] == '(') {
			totalStart++;
		} else if(totalStart == 0) {
			cout << "impossible" << endl;
		} else {
			totalStart--;
		}
	}

	if(totalStart == 0) {
		cout << "possible" << endl;
	} else {
		cout << "impossible" << endl;
	}

	return 0;
}