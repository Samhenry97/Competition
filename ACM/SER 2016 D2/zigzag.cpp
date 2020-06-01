#include <iostream>
#include <cstdio>

using namespace std;

enum zigzag{
  LT,
  EQ,
  GT
};

int main() {
  cin.sync_with_stdio(false);
  cin.tie(nullptr);

  int n;
  scanf("%d", &n);
  int last;
  int len = 1;
  zigzag direction = EQ;
  scanf("%d", &last);
  for(int i = 0; i < n-1; ++i){
    int cur;
    scanf("%d", & cur);
    switch(direction){
      case LT:
        if(cur > last){
          len++;
          direction = GT;
        }
        break;
      case GT:
        if(cur < last){
          len++;
          direction = LT;
        }
        break;
      case EQ:
        if(cur < last){
          len++;
          direction = LT;
        }
        else if(cur > last){
          len++;
          direction = GT;
        }
        break;
    }
    last = cur;
  }
  printf("%d\n", len);
}
