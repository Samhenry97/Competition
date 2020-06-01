#include <iostream>
#include <bitset>
#include <cstdio>

using namespace std;

int main() {
	int n, m;

	scanf("%d %d", &n, &m);
	while(n != 0 && m != 0) {
		int *holdN = new int[n];
		int *holdM = new int[m];
		for(int i = 0; i < n; i++) {
			scanf("%d", &holdN[i]);
		}
		for(int i = 0; i < m; i++) {
			scanf("%d", &holdM[i]);
		}

		int total = 0;
		int nIter = 0, mIter = 0;
		while(nIter < n && mIter < m) {
			if(holdN[nIter] == holdM[mIter]) {
				total++;
				nIter++; mIter++;
			} else if(holdN[nIter] > holdM[mIter]) {
				mIter++;
			} else {
				nIter++;
			}
		}

		printf("%d\n", total);

		scanf("%d %d", &n, &m);
	}

	return 0;
}