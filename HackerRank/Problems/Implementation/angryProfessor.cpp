#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int t;
    cin >> t;
    for(int a0 = 0; a0 < t; a0++){
        int n;
        int k;
        cin >> n >> k;
        vector<int> a(n);
        int onTime = 0;
        for(int a_i = 0;a_i < n;a_i++){
            int temp;
            cin >> temp;
            if(temp <= 0) { onTime++; }
        }
        cout << (onTime >= k ? "NO" : "YES")  << endl;
    }
    return 0;
}
