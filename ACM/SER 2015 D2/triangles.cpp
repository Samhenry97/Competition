#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int x1, y1, z1, x2, y2, z2;
    cin >> x1 >> y1 >> z1;
    cin >> x2 >> y2 >> z2;

    int hyp1 = max(x1, max(y1, z1));
    int hyp2 = max(x2, max(y2, z2));

    int min1 = min(x1, min(y1, z1));
    int min2 = min(x2, min(y2, z2));

    if(min1 != min2) {
        cout << 0;
        return 0;
    }

    if(x1*x1 + y1*y1 + z1*z1 == 2 * hyp1 * hyp1 && x2*x2 + y2*y2 + z2*z2 == 2 * hyp2 * hyp2) {
        if(hyp1 == hyp2) {
            cout << 1;
        } else {
            cout << 0;
        }
    } else {
        cout << 0;
    }

    return 0;

}
