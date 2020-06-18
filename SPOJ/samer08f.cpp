#include <iostream>
    
using namespace std;
    
int main() {
    int dyn[100];
    for(int n = 1; n <= 100; n++) {
        int total = 0;
        for(int i = n; i >= 0; i--) {
            total += i * i;
        }
        dyn[n - 1] = total;
    }
    
    int i; cin >> i;
    while(i != 0) {
        cout << dyn[i - 1] << endl;
        cin >> i;
    }
    
    return 0;
} 