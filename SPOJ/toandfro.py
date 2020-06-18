n = int(input())
    
while n:
    s = input()
    rows = len(s) // n
    ans = []
    
    for x in range(n):
        for y in range(rows):
            ans.append(s[y * n + x if not y & 1 else y * n + n - x - 1])
    print(''.join(ans))
    
    n = int(input()) 