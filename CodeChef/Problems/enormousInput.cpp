#include <stdio.h>

int main() {
	int n, d, count = 0; scanf("%d %d", &n, &d);

	while(n--) {
		int tmp; scanf("%d", &tmp);
		if(tmp % d == 0) { count++; }
	}

	printf("%d\n", count);

	return 0;
}