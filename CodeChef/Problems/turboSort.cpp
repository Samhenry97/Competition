#include <algorithm>
#include <cstdio>

using namespace std;

int data[1000001];

int main() {
	int n; scanf("%d", &n);

	for(int i = 0; i < n; i++) {
		scanf("%d", data + i);
	}

	sort(data, data + n);

	for(int i = 0; i < n; i++) {
		printf("%d\n", data[i]);
	}

	return 0;
}