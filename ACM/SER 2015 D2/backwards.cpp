#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

string strRev(string s) {
    string out = "";
    for(int i = s.length()-1; i >= 0; --i){
        out += s[i];
    }
    return out;
}

int main() {
    int numStrings;
    cin >> numStrings;
    vector<string> strings;
    for(int i = 0; i < numStrings; ++i){
        string str;
        cin >> str;
        str = strRev(str);
        strings.push_back(str);
    }
    sort(strings.begin(), strings.end());
    for(int i = 0; i < strings.size(); ++i){
        cout << strings[i] << endl;
    }
}
