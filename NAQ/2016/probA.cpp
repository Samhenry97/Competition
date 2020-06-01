#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<string> newAlphabet = {"@", "8", "(", "|)", "3", "#", "6", "[-]", "|", "_|", "|<", "1", "[]\\/[]", "[]\\[]", "0", "|D", "(,)", "|Z", "$", "']['", "|_|", "\\/", "\\/\\/", "}{", "`/", "2"};

bool isAlpha(char c) {
	return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z');
}

char toLower(char c) {
	if(c >= 'A' && c <= 'Z') {
		return c - ('A' - 'a');
	}
}

int main() {
	string line;
	string newLine = "";
	getline(cin, line);

	for(int i = 0; i < line.length(); i++) {
		if(isAlpha(line[i])) {
			newLine += newAlphabet[toLower(line[i]) - 'a'];
		} else {
			newLine += line[i];
		}
	}

	cout << newLine;	

	return 0;
}