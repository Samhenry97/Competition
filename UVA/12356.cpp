#include <cstdio>

int left[100001];
int right[100001];

int main() {
	int s, q;

	while(scanf("%d %d", &s, &q), s || q) {
		for(int i = 1; i <= s; i++) {
			left[i] = i - 1;
			right[i] = i + 1;
		}
		left[1] = -1;
		right[s] = -1;

		int f, l;
		while(q--) {
			scanf("%d %d", &f, &l);

			left[right[l]] = left[f];
			right[left[f]] = right[l];

			if(left[f] != -1) {
				printf("%d ", left[f]);
			} else {
				printf("* ");
			}

			if(right[l] != -1) {
				printf("%d\n", right[l]);
			} else {
				printf("*\n");
			}
		}

		printf("-\n");
	}

	return 0;
}