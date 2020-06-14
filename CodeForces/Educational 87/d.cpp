#include <iostream>
using namespace std;

#define MAXN 1000001

int n, q;
int a[MAXN];
int k[MAXN];

int search(int x) {
    int cnt = 0;
    for (int i = 0; i < n; i++) 
        if (a[i] <= x) cnt++;
    for (int i = 0; i < q; i++) {
        if (k[i] > 0 && k[i] <= x) {
            cnt++;
        } else if (k[i] < 0 && abs(k[i]) <= cnt) {
            cnt--;
        }
    }
    return cnt;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(0);
    
    cin >> n >> q;
    for (int i = 0; i < n; i++) cin >> a[i];
    for (int i = 0; i < q; i++) cin >> k[i];

    if (search(1000000000) <= 0) {
        cout << 0 << endl;
        exit(0);
    }

    int bot = 0, top = 1000001;
    while (top - bot > 1) {
        int mid = (top + bot) / 2;
        if (search(mid) > 0) top = mid;
        else bot = mid;
    }

    cout << top << endl;

    return 0;
}