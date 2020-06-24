#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int utopian(int n) {
    int height = 1;
    
    for(int i = 0; i < n; i++) {
        if((i & 0x01) == 0) { height *= 2; }
        else { height += 1; }
    }
    
    return height;
}

int main(){
    int t;
    cin >> t;
    for(int i = 0; i < t; i++){
        int n;
        cin >> n;
        
        cout << utopian(n) << endl;
    }
    return 0;
}
