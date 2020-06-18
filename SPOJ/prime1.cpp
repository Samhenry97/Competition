#include <iostream>
#include <cstring>
#include <cstdlib>
#include <string>
#define ll long long unsigned int
using namespace std;
    
ll power(ll a, ll n, ll mod)
{
    ll power = a;
    ll result = 1;
    
    while (n) {
        if (n & 1) result = ((result % mod) * (power % mod)) % mod;
        power = ((power % mod) * (power % mod)) % mod;
        n >>= 1;
    }
    return result;
}
    
bool witness(ll n, ll s, ll d, ll a) {
    ll x = power(a, d, n);
    ll y;
    
    while (s) {
        y = ((x % n) * (x % n)) % n;
        if (y == 1 && x != 1 && x != n-1) return false;
        x = y;
        s--;
    }
    if (y != 1) return false;
    return true;
}
    
bool isPrime(ll n)
{
    if (((!(n & 1)) && n != 2 ) || (n < 2) || (n % 3 == 0 && n != 3))
        return false;
    if (n <= 3)
        return true;
    
    ll d = n >> 1;
    ll s = 1;
    while (!(d & 1)) {
        d >>= 1;
        s++;
    }
    
    if (n < 1373653)
        return witness(n, s, d, 2) && witness(n, s, d, 3);
    if (n < 9080191)
        return witness(n, s, d, 31) && witness(n, s, d, 73);
    if (n < 4759123141)
        return witness(n, s, d, 2) && witness(n, s, d, 7) && witness(n, s, d, 61);
    if (n < 1122004669633)
        return witness(n, s, d, 2) && witness(n, s, d, 13) && witness(n, s, d, 23) && witness(n, s, d, 1662803);
    if (n < 2152302898747)
        return witness(n, s, d, 2) && witness(n, s, d, 3) && witness(n, s, d, 5) && witness(n, s, d, 7) && witness(n, s, d, 11);
    if (n < 3474749660383)
        return witness(n, s, d, 2) && witness(n, s, d, 3) && witness(n, s, d, 5) && witness(n, s, d, 7) && witness(n, s, d, 11) && witness(n, s, d, 13);
    return witness(n, s, d, 2) && witness(n, s, d, 3) && witness(n, s, d, 5) && witness(n, s, d, 7) && witness(n, s, d, 11) && witness(n, s, d, 13) && witness(n, s, d, 17);
}
    
int main() {
    int n; cin >> n;
    while(n--) {
        int a, b; cin >> a >> b;
        for(int i = a; i <= b; i++) {
            if(isPrime(i)) {
                cout << i << endl;
            }
        }
        cout << endl;
    }
} 