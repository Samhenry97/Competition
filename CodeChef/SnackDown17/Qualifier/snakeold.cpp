#include <cstdio>
#include <algorithm>

using namespace std;

int lens[100001];

int binSearch(int k, int n) {
    int bottom = 0;
    int top = n;
    int middle = n >> 1;
    
    while(top - bottom > 1) {
        if(lens[middle] > k) {
            top = middle;
        } else {
            bottom = middle;
        }
        
        middle = (top + bottom) >> 1;
    }
    
    return middle;
}

int main() {
    int t; scanf("%d", &t);
    
    while(t--) {
        int n, q; scanf("%d %d", &n, &q);
        
        for(int i = 0; i < n; i++) {
            scanf("%d", lens + i);
        }
        
        sort(lens, lens + n);
        
        while(q--) {
            int k; scanf("%d", &k);
            
            if(k <= lens[0]) {
                printf("%d\n", n);
            } else {
                int index = binSearch(k - 1, n);
                int count = n - index - 1;
                int test = 0;
                
                while(test + k - lens[index] <= index) {
                    count += 1;
                    test += k - lens[index];
                    index--;
                }
                
                printf("%d\n", count);
            }
        }
    }
    
    return 0;
}