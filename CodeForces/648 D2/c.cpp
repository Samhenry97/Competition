#include <iostream>
#include <map>
using namespace std;

#define MAXN 200001

int pos[MAXN];
int rot[MAXN];

int main() {
    int n; cin >> n;
    for (int i = 0; i < n; i++) {
        int a; cin >> a;
        pos[a-1] = i;
    }
    int ans = 0;
    for (int i = 0; i < n; i++) {
        int b; cin >> b;
        int move = (i + n - pos[b-1]) % n;
        rot[move]++;
        ans = max(ans, rot[move]);
    }

    cout << ans << endl;

    return 0;
}