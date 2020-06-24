#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;
    
    for(int i = 0; i < n; i++) {
        int a, b;
        cin >> a >> b;
        
        int count = 0;
        long test = 0;
        while(true) {
            long ans = test * test;
            if(ans > 1000000000L) { break; }
            if(ans > b) { break; }
            if(a <= ans && ans <= b) { count++; }
            test++;
        }
        
        cout << count << endl;
    }
    
    return 0;
}
