#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
  int b, p;
  cin >> b >> p;
  int bars[b];
  int plates[p];
  for (int i = 0; i < b; i ++) {
    cin >> bars[i];
  }
  for (int i = 0; i < p; i ++) {
    cin >> plates[i];
  }

  int pow = 1;
  for (int i = 0; i < p; i ++) {
    pow *= 3;
  }
  vector<int> possibilities;
  for (int i = 0; i < pow; i++) {
      int left = 0;
      int right = 0;
      int k = i;
      for (int j = 0; j < p; j++) {
        switch (k % 3) {
          case 0: left  += plates[j]; break;
          case 1: right += plates[j]; break;
          case 2: break;
        }

        k /= 3;
      }
      if (left == right) {
        for (int j: bars) {
          possibilities.push_back(left + right + j);
        }
      }
  }

  sort(possibilities.begin(), possibilities.end());
  auto last = 0;
  for (auto i: possibilities) {
    if (i != last) {
      cout << i << endl;
    }
    last = i;
  }
}
