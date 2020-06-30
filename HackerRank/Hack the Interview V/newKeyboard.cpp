#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false); cin.tie(0);
    string s; getline(cin, s);
    
    list<char> ans;
    auto idx = ans.begin();
    bool num = true;
    for (char c : s) {
        if (c == '*') {
            if (idx != ans.begin()) {
                idx--;
                idx = ans.erase(idx);
            }
        } else if(c == '<') {
            idx = ans.begin();
        } else if(c == '>') {
            idx = ans.end();
        } else if(c == '#') {
            num = !num;
        } else if ('0' <= c && c <= '9') {
            if (num) {
                idx = ans.insert(idx, c);
                idx++;
            }
        } else {
            idx = ans.insert(idx, c);
            idx++;
        }
    }
    
    for (char c : ans) cout << c;
    cout << endl;

    return 0;
}