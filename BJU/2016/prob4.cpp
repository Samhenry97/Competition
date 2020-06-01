#include <iostream>
#include <algorithm>
#include <cstdio>
#include <queue>
#include <stack>
#include <unordered_map>
#include <map>
#include <vector>
#include <string>

using namespace std;

string telegram(string s) {
	string ans = "";

	for(int i = 0; i < s.length(); i++) {
		if(s[i] == '\t') {
			ans += " ";
		} else if(s[i] == '.') {
			ans += " STOP ";
		} else if(s[i] == ',') {
			ans += " CMA ";
		} else if(s[i] == '!') {
			ans += " HEY ";
		} else if(s[i] == '?') {
			ans += " HUH ";
		} else {
			ans += toupper(s[i]);
		}
	}

	//front trim
	while(ans.size() != 0 && (ans[0] == ' ' || ans[0] == '\t')) {
		ans.erase(0, 1);
	}

	//back trim
	while(ans.size() != 0 && (ans[ans.size() - 1] == ' ' || ans[ans.size() - 1] == '\t')) {
		ans.erase(ans.size() - 1, 1);
	}

	int white = 0;
	int size = ans.length();
	for(int i = 0; i < size; i++) {
		if(ans[i] == '\t' || ans[i] == ' ') {
			if(white == 0) {
				white++;
			} else {
				ans.erase(i, 1);
				size--;
				i--;
			}
		} else {
			white = 0;
		}
	}

	ans += " END";
	return ans;
}

int main() {
	int n;
	cin >> n;

	string line;
	getline(cin, line);
	for(int i = 0; i < n; i++) {
		getline(cin, line);
		cout << telegram(line) << endl;
	}

	return 0;
}