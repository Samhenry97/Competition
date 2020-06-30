#include <iostream>
#include <string>
#include <stack>
using namespace std;

int main() {
    ios::sync_with_stdio(false); cin.tie(0);
    int t; cin >> t;
    while(t--) {
        string s; cin >> s;
        stack<char> st;
        int ans = 0;
        for (char c : s) {
            if (st.size() && st.top() == c) {
                ans ++;
                st.pop();
            } else {
                st.push(c);
            }
        }
        cout << ans << endl;
    }

    return 0;
}