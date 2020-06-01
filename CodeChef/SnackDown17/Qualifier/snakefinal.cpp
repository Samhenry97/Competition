#include <stdio.h>
#include <stdlib.h>

long long lens[100001];
long long sums[100001];

int cmp(const void *a, const void *b) {
    long long av = (*(long long *) a);
    long long bv = (*(long long *) b);

    if(av < bv) {
        return -1;
    } else if(bv < av) {
        return 1;
    } else {
        return 0;
    }
}

long long getIndex(long long k, long long n) { // Binary search for index
    long long bottom = 0;
    long long top = n;
    long long middle = n >> 1;
    
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

long long solve(long long k, long long n, long long index) {
    long long count = n - index - 1;
    long long topSum = sums[index + 1];
    
    long long top = index;
    long long bottom = 0;
    long long middle = index >> 1;
    
    while(top - bottom > 1) {
        long long dist = index - middle + 1;
        if(k * dist - (sums[middle] - topSum) <= middle) { // Works
            top = middle;
        } else {
            bottom = middle;
        }
        
        middle = (top + bottom) >> 1;
    }
    
    long long low = k * (index - bottom + 1) - (sums[bottom] - topSum);
    long long high = k * (index - top + 1) - (sums[top] - topSum);
    
    if(low <= bottom) {
        return count + index - bottom + 1;
    } else if(high <= top) {
        return count + index - top + 1;
    } else {
        return count;
    }
}

int main() {
    long long t; scanf("%lld", &t);
    
    while(t--) {
        long long n, q; scanf("%lld %lld", &n, &q);
        
        for(long long i = 0; i < n; i++) {
            scanf("%lld", lens + i);
        }
        
        qsort(lens, n, sizeof(long long), cmp);
        
        sums[n - 1] = lens[n - 1];
        for(long long i = n - 2; i >= 0; i--) {
            sums[i] = sums[i + 1] + lens[i];
        }
        
        while(q--) {
            long long k; scanf("%lld", &k);
            
            if(k <= lens[0]) {
                printf("%lld\n", n);
            } else {
                long long index = getIndex(k - 1, n);
                
                printf("%lld\n", solve(k, n, index));
            }
        }
    }
    
    return 0;
}