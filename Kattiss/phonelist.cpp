#include <iostream>
#include <string>
#include <vector>

using namespace std;

struct Node {
	Node** data;
	bool isLast;
	Node(bool isLastInit=false) : data(new Node*[10]), isLast(isLastInit) { 
		for(int i = 0; i < 10; i++) {
			data[i] = nullptr;
		} 
	}
	bool addNode(string number) {
		if(number.length() > 1) {
			Node *cur = data[number[0] - '0'];
			if(cur != nullptr) {
				if(cur->isLast) { return false; }
				return data[number[0] - '0']->addNode(number.substr(1));
			} else {
				cur = new Node();
				data[number[0] - '0'] = cur;
				return cur->addNode(number.substr(1));
			}
		} else {
			Node *cur = data[number[0] - '0'];
			if(cur != nullptr) {
				return false;
			} else {
				cur = new Node(true);
				data[number[0] - '0'] = cur;
				return true;
			}
		}
	}
};

int main() {
	int n;
	cin >> n;

	while(n--) {
		Node *root = new Node();
		int total = 0;
		string number;
		cin >> total;

		bool prefix = false;
		while(total--) {
			cin >> number;
			if(!prefix && !root->addNode(number)) {
				prefix = true;
			}
		}

		if(prefix) { cout << "NO" << endl; }
		else { cout << "YES" << endl; }
	}

	return 0;
}