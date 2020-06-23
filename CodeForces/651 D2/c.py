import math
  
def factorize(n): 
    ans = []
    while n % 2 == 0: 
        ans.append(2)
        n = n // 2
    for i in range(3, int(math.sqrt(n)) + 1, 2): 
        while n % i == 0: 
            ans.append(i)
            n = n // i 
    if n > 2: 
        ans.append(n)
    return ans

for i in range(int(input())):
    n = int(input())
    fact = factorize(n)
    turn = False

    if n == 1:
        print('FastestFinger')
    elif n == 2:
        print('Ashishgup')
    elif 2 in fact and any([x % 2 == 1 for x in fact]):
        if fact.count(2) > 1 or len([x for x in fact if x % 2 == 1]) > 1:
            print('Ashishgup')
        else:
            print('FastestFinger')
    elif n % 2 != 0:
        print('Ashishgup')
    else:
        print('FastestFinger')