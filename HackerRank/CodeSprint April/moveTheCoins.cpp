#include <iostream>
#include <vector>

using namespace std;

struct Node;

vector<Node> nodes;

struct Node {
	int depth;
	int coins;
	int parIndex;
	vector<int> children;
	Node() : depth(-1), coins(0), parIndex(-2) { ; }
	Node(int initDepth, int initCoins, int initParIndex)
		: depth(initDepth), coins(initCoins), parIndex(initParIndex) { ; }
	void updateDepth() {
		depth = nodes[parIndex].depth + 1;
		for(int i = 0; i < children.size(); i++) {
			nodes[children[i]].updateDepth();
		}
	}
};

int main() {
	int numNodes;
	cin >> numNodes;

	nodes = vector<Node>(numNodes);
	vector<int> coins(numNodes);
	for(int i = 0; i < numNodes; i++) {
		cin >> coins[i];
	}

	nodes[0] = Node(0, 0, -1);
	int first, second;
	for(int i = 0; i < numNodes - 1; i++) {
		cin >> first >> second;
		first--; second--;

		nodes[second] = Node(nodes[first].depth + 1, coins[second], first);
		nodes[first].children.push_back(second);
	}

	int queries;
	cin >> queries;
	for(int i = 0; i < queries; i++) {
		cin >> first >> second;
		first--; second--;

		//Test to make sure it does not create a cycle.
		bool legal = true;
		int parent = nodes[second].parIndex;
		while(legal && parent != -1) {
			if(first == parent) {
				cout << "INVALID\n";
				legal = false;
				break;
			} else {
				parent = nodes[parent].parIndex;
			}
		}
		if(!legal) { continue; }

		int oldParIndex = nodes[first].parIndex;

		//Move it to the new parent!
		nodes[first].parIndex = second;
		nodes[first].updateDepth();

		int moves = 0;
		for(int i = 0; i < nodes.size(); i++) {
			Node cur = nodes[i];
			moves += cur.depth;
		}
		if(moves & 1) { //Odd
			cout << "YES\n";
		} else {
			cout << "NO\n";
		}

		//Restore the tree back to its old parent
		nodes[first].parIndex = oldParIndex;
		nodes[first].updateDepth();
	}

	return 0;
}