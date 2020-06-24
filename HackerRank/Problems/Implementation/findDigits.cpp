#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

void getNums(int n, vector<int> &ans) {
    while(n >= 10) {
        ans.push_back(n % 10);
        n /= 10;
    }
    ans.push_back(n);
}

int main(){
    int t;
    cin >> t;
    for(int i = 0; i < t; i++){
        int n;
        int count = 0;
        cin >> n;
        
        vector<int> nums;
        getNums(n, nums);
        for(int j = 0; j < nums.size(); j++) {
            if(nums[j] == 0) { continue; }
            if(n % nums[j] == 0) { count++; }
        }
        cout << count << endl;
    }
    return 0;
}
