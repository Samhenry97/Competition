#include <cstdio>

using namespace std;

typedef unsigned long long ull;

int fastExp(int n, int x) {
	ull ans = 1, binPow = n;
	while(x > 0) {
		if(x & 1) { ans = (ans * binPow) % 1000000007; }
		binPow = (binPow * binPow) % 1000000007;
		x >>= 1;
	}
	return ans;
}

void calc(int a, int b) {
	if(a == 1) { printf("%d %d\n", 0, 1); return; }

	int k = 1;
	while(k < 1e8) {
		int top = 1e8, bottom = 0, n = top >> 1;
		while(top - bottom > 1) {
			ull ans = fastExp((n + 1), k);
			if(ans == a && fastExp(n, k) == b) {
				int count = 1;
				for(int i = 1; i < k; i++) { count += fastExp(n, k - i); }
				int height = a, curHeight = a, levelTotal = 1;
				for(int i = 0; i < k; i++) { 
					curHeight /= n + 1;
					levelTotal *= n;
					height += curHeight * levelTotal;
				}
				printf("%d %d\n", count, height);
				return;
			} else if(ans > a) { 
				top = n; 
			} else {
				bottom = n;
			}
			n = (top + bottom) >> 1;
		}
		k++;
	}
}

int main() {
	int a, b; scanf("%d%d", &a, &b);

	while(a || b) {
		calc(a, b);
		scanf("%d%d", &a, &b);
	}

	return 0;
}