#include <vector>
#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

typedef long long int ll;

int grid[100][100];

int main() {
    int t; cin >> t;
    while(t--) {
        int x1, y1, x2, y2; 
        cin >> x1 >> y1 >> x2 >> y2;
        x1--; y1--; x2--; y2--;
        ll n = abs(y2 - y1) + 1;
        ll m = abs(x2 - x1) + 1;
        ll a = n-1;
        cout << 1LL + a * (m - 1LL) << endl;
    }

    return 0;
}