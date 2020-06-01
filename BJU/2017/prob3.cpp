#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int main() {
	string s1, s2, s3;
	cin >> s1 >> s2 >> s3;
	int a = 0, b = 0, c = 0;

	while(true) {
		int one = 0, two = 0, three = 0;
		for(int i = 0; i < 5; i++) {
			if(s1[i] == 'A') {
				one += pow(10, 5 - i - 1) * a;
			} else if(s1[i] == 'B') {
				one += pow(10, 5 - i - 1) * b;
			} else if(s1[i] == 'C') {
				one += pow(10, 5 - i - 1) * c;
			} else {
				one += pow(10, 5 - i - 1) * (s1[i] - '0');
			}
		}

		for(int i = 0; i < 5; i++) {
			if(s2[i] == 'A') {
				two += pow(10, 5 - i - 1) * a;
			} else if(s2[i] == 'B') {
				two += pow(10, 5 - i - 1) * b;
			} else if(s2[i] == 'C') {
				two += pow(10, 5 - i - 1) * c;
			} else {
				two += pow(10, 5 - i - 1) * (s2[i] - '0');
			}
		}

		for(int i = 0; i < 5; i++) {
			if(s3[i] == 'A') {
				three += pow(10, 5 - i - 1) * a;
			} else if(s3[i] == 'B') {
				three += pow(10, 5 - i - 1) * b;
			} else if(s3[i] == 'C') {
				three += pow(10, 5 - i - 1) * c;
			} else {
				three += pow(10, 5 - i - 1) * (s3[i] - '0');
			}
		}

		if(one + two == three) {
			s1 = to_string(one);
			s2 = to_string(two);
			s3 = to_string(three);
			while(s1.length() < 5) { s1 = '0' + s1; }
			while(s2.length() < 5) { s2 = '0' + s2; }
			while(s3.length() < 5) { s3 = '0' + s3; }
			cout << s1 << endl << s2 << endl << s3 << endl;
			break;
		}

		a += 1;
		if(a == 10) {
			a = 0;
			b += 1;
			if(b == 10) {
				b = 0;
				c += 1;
			}
			if(c == 10) {
				break;
			}
		}
	}
}