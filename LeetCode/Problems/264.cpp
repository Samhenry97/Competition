typedef long long int ll;

class Solution {
public:
    int nthUglyNumber(int n) {
        set<ll> found; found.insert(1);
        while (--n) {
            ll cur = *found.begin(); found.erase(found.begin());
            found.insert(cur * 2);
            found.insert(cur * 3);
            found.insert(cur * 5);
        }
        return *found.begin();
    }
};