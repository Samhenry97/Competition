#include <iostream>
#include <string>
#include <map>

using namespace std;

int main() {
    string str;
    getline(cin, str);
    int high = 0, high2 = 0;

    map<char, int> vals;

    for(int i = 0; i < str.length(); i++) {
        vals[str[i]] += 1;
        if(vals[str[i]] > high && vals[str[i]] != high) {
            high = vals[str[i]];
        } else if(vals[str[i]] > high2 && vals[str[i]] != high2) {
            high2 = vals[str[i]];
        }
    }

    if(vals.size() > 2) {
        cout << str.length() - (high + high2);
    } else {
        cout << 0;
    }

    return 0;
}
