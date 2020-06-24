#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int n, t;
    cin >> n >> t;
    vector<int> width(n);
    for(int width_i = 0;width_i < n; width_i++){
       cin >> width[width_i];
    }
    
    for(int a = 0; a < t; a++){
        int i, j;
        cin >> i >> j;
        
        int max = 3;
        for(; i <= j; i++) {
            if(width[i] < max) { max = width[i]; }
            if(max == 1) { break; }
        }
        
        cout << max << endl;
    }
    return 0;
}
