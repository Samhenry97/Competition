#include <iostream>
#include <cmath>
#include <algorithm>
    
using namespace std;
    
typedef long double ld;
typedef long long int ll;
    
ld h, c, t;
    
ld calc(ll mid) {
    ll cnt = mid * 2 + 1;
    ld tmp = (h * (mid+1) + c * mid) / cnt;
    return tmp;
}
    
int tc() {
    cin >> h >> c >> t;
    if (h == t) {
        return 1;
    } else if((h + c) / 2 == t) {
        return 2;
    }
    
    ll bot = 0, top = 1000000000;
    while (top - bot > 1) {
        ll mid = (bot + top) / 2;
        if (calc(mid) > t) {
            bot = mid;
        } else {
            top = mid;
        }
    }
    
    ld tmp1 = abs(t-calc(bot));
    ld tmp2 = abs(t-calc(top));
    ld tmp; ll cnt;
    if (tmp1 <= tmp2) {
        tmp = tmp1;
        cnt = bot * 2 + 1;
    } else {
        tmp = tmp2;
        cnt = top * 2 + 1;
    }
    ld base = abs(t-((h+c)/2L));
    if (base == tmp) {
        if (cnt < 2) {
            return cnt;
        }
        return 2;
    } else if(base < tmp) {
        return 2;
    } else {
        return cnt;
    }
}
    
int main() {
    int t; cin >> t;
    while (t--) {
        cout << tc() << endl;
    }
    return 0;
}