#include <queue>
#include <cstdio>

using namespace std;

int a[100001];
int b[100001];
int f[100001];

struct Node {
	int a, b, i;
	Node(int ai, int bi, int ii) : a(ai), b(bi), i(ii) { ; }
};

int main() {
	int t; scanf("%d", &t);

	while(t--) {
		int n; scanf("%d", &n);

		for(int i = 0; i < n; i++) { scanf("%d", a + i); }
		for(int i = 0; i < n; i++) { scanf("%d", b + i); }

		queue<Node> nodes;
		for(int i = 0; i < n; i++) {
			nodes.push(Node(a[i], b[i], i));
		}

		while(!nodes.empty()) {
			Node &tmp = nodes.front();
			printf("%d %d\n", tmp.a, tmp.b);
			nodes.pop();
		}
	}

	return 0;
}