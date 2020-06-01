#include "bits/stdc++.h"
using namespace std;

typedef long double ld;

ld x[100001];
ld v[100001];
int n;

ld span(ld time) {
	ld left = numeric_limits<ld>::max();
	ld right = numeric_limits<ld>::min();
	for(int i = 0; i < n; i++) {
		ld pos = x[i] + time * v[i];
		left = min(left, pos);
		right = max(right, pos);
	}
	return right - left;
}

int main() {
	ios::sync_with_stdio(false);
	scanf("%d", &n);

	for(int i = 0; i < n; i++) {
		scanf("%Lf", x + i);
		scanf("%Lf", v + i);
	}

	bool iter = false;
	ld prev = 0, low = 0, high = 1000000;
	while(true) {
		ld lmid = (2 * low + high) / 3;
		ld rmid = (low + 2 * high) / 3;
		ld lres = span(lmid);
		ld rres = span(rmid);
		if(lres > rres) { low = lmid; }
		else { high = rmid; }
		if(iter && abs(prev - lres) < 0.000000001) { break; }
		iter = true;
		prev = lres;
	}

	printf("%.4Lf\n", prev);
}