#include <bits/stdc++.h>
using namespace std;

#define INF 0x7FFFFFFF

int a[20001];

int main() {
    ios::sync_with_stdio(false);
    int t; cin >> t;
    
    while(t--) {
        int s, e; cin >> s >> e;
        int minx = INF, miny = INF, ansx = 0, ansy = 0;
        multimap<int, int> vals;
        for(int i = 0; i < e; i++) {
            cin >> a[i];
            vals.insert(make_pair(a[i], i));
        }
        
        for(int i = 0; i < e; i++) {
            int test = s - a[i];
            auto ret = vals.equal_range(test);
            for(auto it = ret.first; it != ret.second; it++) {
                if(it->second != i) {
                    int other = it->second;
                    int far = max(i, other);
                    int near = min(i, other);
                    if(far < miny || (far == miny && near < minx)) {
                        miny = far;
                        minx = near;
                        ansx = min(a[i], a[other]);
                        ansy = max(a[i], a[other]);
                    }
                }
            }
        }
        
        if(minx == INF) {
            cout << "!OK" << endl;
        } else {
            cout << ansx << " " << ansy << endl;;
        }
    }
    
    return 0;
}