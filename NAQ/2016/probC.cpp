#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct Node {
	int origin;
	int id;
	int weight;
};

void tweakedDijkstras(vector<vector<Node*>> &nodes, vector<int> &items) {
	queue<Node*> q;

	int start = 0, end = nodes.size() - 1;
	vector<int> distances(nodes.size(), -1);
	vector<int> maxItems(nodes.size(), 0);

	distances[start] = 0;
	maxItems[start] = items[start];

	for(int i = 0; i < nodes[start].size(); i++) {
		q.push(nodes[start][i]);
	}

	while(!q.empty()) {
		Node *top = q.front(); q.pop();

		int newDistance = distances[top->origin] + top->weight;
		int newItems = maxItems[top->origin] + items[top->id];

		if(distances[top->id] == -1) {
			distances[top->id] = newDistance;
			maxItems[top->id] = newItems;
		} else if(newDistance < distances[top->id]) {
			distances[top->id] = newDistance;
			maxItems[top->id] = newItems;
		} else if(distances[top->id] == newDistance && newItems > maxItems[top->id]) {
			maxItems[top->id] = newItems;
		}

		for(int i = 0; i < nodes[top->id].size(); i++) {
			Node *cur = nodes[top->id][i];

			int newDistance = distances[top->id] + cur->weight;
			int newItems = maxItems[top->id] + items[cur->id];

			if((distances[cur->id] == -1)
				|| (newDistance < distances[cur->id])
				|| (newDistance == distances[cur->id] && newItems > maxItems[cur->id])) {
				q.push(nodes[top->id][i]);
			}
		}
	}

	if(distances[nodes.size() - 1] == -1) {
		cout << "impossible" << endl;
	} else {
		cout << distances[nodes.size() - 1] << " " << maxItems[nodes.size() - 1] << endl;
	}
}

int main() {
	int numNodes;
	cin >> numNodes;

	vector<int> items(numNodes);
	vector<vector<Node*>> nodes(numNodes);

	for(int i = 0; i < numNodes; i++) {
		cin >> items[i];
	}

	int numEdges;
	cin >> numEdges;

	for(int i = 0; i < numEdges; i++) {
		Node *newNode = new Node();
		int a, b, d;
		cin >> a >> b >> d;
		a--; b--;
		newNode->id = b;
		newNode->weight = d;
		newNode->origin = a;
		nodes[a].push_back(newNode);
	}

	tweakedDijkstras(nodes, items);

	return 0;
}