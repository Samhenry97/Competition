#include <iostream>
#include <string>
using namespace std;

int main() {
    int brk, safe, floor, numDrops, floors;
    string state;
    cin >> numDrops >> floors;
    brk = 2;
    safe = floors -1 ;
    int maxSafe = 0, minBreak = floors;
    for (int i = 0; i < numDrops; ++i){
        cin >> floor >> state;
        if(state == "BROKEN"){
            if(floor <= safe) { safe = floor-1; }
            if (floor < minBreak) {minBreak = floor;}
        } else {
            if(floor >= brk) { brk = floor+1; }
            if (floor > maxSafe) { maxSafe = floor;}
        }
    }
    cout << brk << " ";
    /*if(brk - 1 > safe) { cout << brk -1; }
    else {
        cout << safe;
    }*/
    cout << safe;
}
