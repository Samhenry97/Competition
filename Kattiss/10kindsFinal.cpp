#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <bitset>

using namespace std;

template<typename Key>
class DisjointSet {
    std::vector<int> parent;

public:
    int findOrAddKey(const Key& key) {
    	parent.push_back(-1);
    	return parent.size() - 1;
    }

    int find(int v) {
        int root = parent[v];
        while (root >= 0) {
            v = parent[v];
            root = parent[v];
        }
        return v;
    }

    int merge(int u, int v) {
        u = find(u);
        v = find(v);

        if (u == v) { return (int)(-parent[v]); }
        
        if (parent[u] < parent[v]) {
            parent[u] += parent[v];
            parent[v] = u;
            return (int)(-parent[u]);
        } else {
            parent[v] += parent[u];
            parent[u] = v;
            return (int)(-parent[v]);
        }
    }
};

int main() {
	int r, c;
	cin >> r >> c;

	DisjointSet<int> set;
	vector<char> bits(r * c, 0);

	for(int i = 0; i < r * c; i++) {
		set.findOrAddKey(i);
	}

	string cur;
	string last;

	cin >> cur;
	bits[0] = cur[0];
	for(int i = 1; i < cur.length(); i++) {
		bits[i] = cur[i];
		if(cur[i] == cur[i - 1]) {
			set.merge(i, i - 1);
		}
	}

	last = cur;

	for(int y = 1; y < r; y++) {
		cin >> cur;
		bits[y * c] = cur[0];
		if(last[0] == cur[0]) {
			set.merge(y * c - c, y * c);
		}
		for(int x = 1; x < cur.length(); x++) {
			bits[y * c + x] = cur[x];
			if(cur[x] == last[x]) {
				set.merge(y * c + x, y * c + x - c);
			}
			if(cur[x] == cur[x - 1]) {
				set.merge(y * c + x, y * c + x - 1);
			}
		}
		last = cur;
	}

	int test;
	cin >> test;

	for(int i = 0; i < test; i++) {
		int x1, y1, x2, y2;
		cin >> y1 >> x1 >> y2 >> x2;
		x1--; y1--; x2--; y2--;

		int par1 = set.find(y1 * c + x1);
		int par2 = set.find(y2 * c + x2);

		if(par1 == par2) {
			if(bits[y1 * c + x1] == '0') {
				cout << "binary" << endl;
			} else {
				cout << "decimal" << endl;
			}
		} else {
			cout << "neither" << endl;
		}
	}

	return 0;
}