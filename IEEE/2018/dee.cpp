#include <bits/stdc++.h>
using namespace std;

int n, choices[36];
stack<char> s1, s2;
int s1c, s2c;
string s;

void recurse(int i) {
    if(s1c > n / 2 || s2c > n / 2) return;
    if(i == n) {
        if(s1c == s2c && !s1.size() && !s2.size()) {
            for(int i = 0; i < n; i++) {
                cout << choices[i] << " ";
            }
            exit(0);
        }
        return;
    }
    
    if(s[i] == '(' || s[i] == '[') {
        s1.push(s[i]);
        s1c++;
        choices[i] = 1;
        recurse(i + 1);
        s1.pop();
        s1c--;
        
        s2.push(s[i]);
        s2c++;
        choices[i] = 2;
        recurse(i + 1);
        s2.pop();
        s2c--;
    } else { // Close
        if(s1.size()) {
            char tmp = s1.top();
            if((tmp == '[' && s[i] == ']') || (tmp == '(' && s[i] == ')')) {
                s1.pop();
                s1c++;
                choices[i] = 1;
                recurse(i + 1);
                s1.push(tmp);
                s1c--;
            }
        }
        
        if(s2.size()) {
            char tmp = s2.top();
            if((tmp == '[' && s[i] == ']') || (tmp == '(' && s[i] == ')')) {
                s2.pop();
                s2c++;
                choices[i] = 2;
                recurse(i + 1);
                s2.push(tmp);
                s2c--;
            }
        }
    }
}

int main() {
    cin >> s; n = s.length();
    
    int open = 0;
    for(int i = 0; i < n; i++) {
        if(s[i] == '(' || s[i] == '[') {
            open++;
        }
    }
    
    if(open == n / 2) {
        recurse(0);
    }
    cout << "impossible" << endl;
    
    return 0;
}