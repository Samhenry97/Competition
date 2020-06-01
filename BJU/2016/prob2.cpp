#include <iostream>
#include <algorithm>
#include <cstdio>
#include <queue>
#include <stack>
#include <unordered_map>
#include <map>
#include <vector>

using namespace std;

struct C {
	int freq;
	char c;
	C(char ic, int ifreq) : c(ic), freq(ifreq) { ; }
};

class CC {
public:
	bool operator()(C &first, C &second) {
		return (first.freq < second.freq);
	}
};

int main() {
	unordered_map<char, int> letters;
	vector<char> tops;
	vector<char> order;
	char c;
	int freq = 0;
	while(cin >> c) {
		if(find(order.begin(), order.end(), c) == order.end()) {
			order.push_back(c);
		}
		letters[c]++;
		if(letters[c] > freq) {
			freq = letters[c];
			tops.clear();
			tops.push_back(c);
		} else if(letters[c] == freq) {
			tops.push_back(c);
		}
	}
	for(int i = 0; i < order.size(); i++) {
		if(find(tops.begin(), tops.end(), order[i]) != tops.end()) {
			cout << order[i];
		}
	}

	return 0;
}