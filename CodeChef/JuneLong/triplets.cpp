#include <cstdio>
#include <algorithm>
#include <functional>

using namespace std;

typedef unsigned long long ull;

ull p[100001];
ull q[100001];
ull r[100001];

int main() {
	int t; scanf("%d", &t);
	int a, b, c; scanf("%d %d %d", &a, &b, &c);

	for(int i = 0; i < a; i++) { scanf("%llu", p + i); }
	for(int i = 0; i < b; i++) { scanf("%llu", q + i); }
	for(int i = 0; i < c; i++) { scanf("%llu", r + i); }

	sort(p, p + a);
	sort(q, q + b, greater<ull>());
	sort(r, r + c);

	ull sum = 0;

	int ai = 0;
	while(ai < a) {
		int bi = 0;
		while(bi < b && p[ai] <= q[bi]) {
			int ci = 0;
			ull curSum = p[ai] + q[bi];
			while(ci < c && q[bi] >= r[ci]) {
				sum = (sum + (curSum * (q[bi] + r[ci]))) % 1000000007ULL;
				ci++;
			}
			bi++;
		}
		ai++;
	}

	printf("%llu\n", sum);

	return 0;
}