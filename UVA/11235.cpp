#include "bits/stdc++.h"
#define MAXN 100001
using namespace std;

int input[MAXN];
int freq[MAXN];

struct SegmentTree {
	vector<int> tree;
	vector<int> data;

	SegmentTree(vector<int> init) {
		data = init;
		tree = vector<int>(init.size() << 2);
		build(1, 0, init.size() - 1);
	}

	void build(int p, int l, int r) {
		if(l == r) { tree[p] = l; }
		else {
			int left = p << 1;
			int right = (p << 1) + 1;
			build(left, l, (l + r) >> 1);
			build(right, ((l + r) >> 1) + 1, r);
			int lVal = data[tree[left]];
			int rVal = data[tree[right]];
			tree[p] = lVal >= rVal ? tree[left] : tree[right];
		}
	}

	int query(int p, int l, int r, int i, int j) {
		if(i > r || j < l) { return -1; }
		if(i <= l && j >= r) { return tree[p]; }
		int p1 = query(p << 1, l, (l + r) >> 1, i, j);
		int p2 = query((p << 1) + 1, ((l + r) >> 1) + 1, r, i, j);
		if(p1 == -1) { return p2; }
		if(p2 == -1) { return p1; }
		return data[p1] >= data[p2] ? p1 : p2;
	}

	int query(int i, int j) {
		return query(1, 0, data.size() - 1, i, j);
	}
};

int main() {
	int n;
	while(scanf("%d", &n) && n) {
		int q; scanf("%d", &q);
		freq[0] = 1;
		map<int, int> end;
		for(int i = 0; i < n; i++) {
			int tmp; scanf("%d", &tmp);
			input[i] = tmp;
			if(i) {
				if(input[i] == input[i - 1]) {
					freq[i] = freq[i - 1] + 1;
				} else {
					freq[i] = 1;
				}
			}
			end[input[i]] = i;
		}

		SegmentTree st(vector<int>(freq, freq + n));
		while(q--) {
			int a, b; scanf("%d%d", &a, &b); a--; b--;
			if(a == 0 && b == n - 1) {
				printf("%d\n", st.data[st.query(a, b)]);
			} else if(input[a] == input[b]) {
				printf("%d\n", b - a + 1);
			} else {
				int ans = end[input[a]] - a + 1;
				ans = max(ans, st.data[st.query(end[input[a]] + 1, b)]);
				printf("%d\n", ans);
			}
		}
	}

	return 0;
}