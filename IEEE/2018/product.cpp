#include <bits/stdc++.h>
using namespace std;

typedef long long int ll;

ll a[2000], b[2000];
ll grid[2000][2000];
ll n, m;

ll kadane(ll* arr, ll* start, ll* finish, ll n) {
    ll sum = 0, maxSum = LLONG_MIN, i; 
    *finish = -1; 
    ll local_start = 0; 
  
    for (i = 0; i < n; ++i) { 
        sum += arr[i]; 
        if (sum < 0) { 
            sum = 0; 
            local_start = i+1; 
        } else if (sum > maxSum) { 
            maxSum = sum; 
            *start = local_start; 
            *finish = i; 
        } 
    } 
  
    if (*finish != -1) 
        return maxSum; 
  
    maxSum = arr[0]; 
    *start = *finish = 0; 
   
    for (i = 1; i < n; i++) { 
        if (arr[i] > maxSum) { 
            maxSum = arr[i]; 
            *start = *finish = i; 
        } 
    } 
    return maxSum; 
} 
  
ll findMaxSum() { 
    ll maxSum = LLONG_MIN, finalLeft, finalRight, finalTop, finalBottom; 
  
    ll left, right, i; 
    ll temp[n], sum, start, finish; 
  
    for (left = 0; left < m; ++left) { 
        memset(temp, 0, sizeof(temp)); 
  
        for (right = left; right < m; ++right) { 
            for (i = 0; i < n; ++i) 
                temp[i] += grid[i][right]; 
            sum = kadane(temp, &start, &finish, n); 
  
            if (sum > maxSum) { 
                maxSum = sum; 
                finalLeft = left; 
                finalRight = right; 
                finalTop = start; 
                finalBottom = finish; 
            } 
        } 
    } 
  
    return maxSum;
} 

int main() {
    ios::sync_with_stdio(false);
    cin >> n >> m;
    for(int i = 0; i < n; i++) { cin >> a[i]; }
    for(int i = 0; i < m; i++) { cin >> b[i]; }
    
    for(int y = 0; y < n; y++) {
        for(int x = 0; x < m; x++) {
            grid[y][x] = a[y] * b[x];
        }
    }
    
    cout << findMaxSum() << endl;
    
    return 0;
}