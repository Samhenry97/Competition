#include <iostream>
#include <string>

using namespace std;

bool isPalindrome(string s) {
	for(int i = 0; i < s.length() / 2; i++) {
		if(s[i] != s[s.length() - i - 1]) return false;
	}
	return true;
}

void calcPalindrome(long num) {	
	string cur = to_string(num);
	int iter = 0;
	while(!isPalindrome(cur)) {
		string temp(cur.length(), ' ');
		for(int i = 0; i < cur.length(); i++) {
			temp[cur.length() - i - 1] = cur[i];
		}
		long nextNum = stoi(temp);
		num = nextNum + num;
		cur = to_string(num);
		iter++;
	}
	cout << iter << " " << num << endl;
}

int main() {
	int n;
	long num;
	cin >> n;

	while(n--) {
		cin >> num;
		calcPalindrome(num);
	}

	return 0;
}