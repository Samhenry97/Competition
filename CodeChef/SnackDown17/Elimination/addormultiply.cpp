#include <cstdio>

using namespace std;

typedef unsigned long long ull;

ull e[100001];

int main() {
	int t; scanf("%d", &t);

	while(t--) {
		int n; scanf("%d", &n);

		for(int i = 0; i < n; i++) { scanf("%llu", e + i); }

		ull sum = 0;
		ull times = n - 1;
		for(int i = 0; i < n - 1; i++) {
			sum += (e[i] + e[i + 1]) * times;
			sum += (e[i] * e[i + 1]) * times;
		}

		printf("%llu\n", sum);
	}

	return 0;
}