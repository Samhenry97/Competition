n = int(input())
while n != -1:
    l = [int(input()) for _ in range(n)]
    
    if sum(l) % len(l) == 0:
        mean = sum(l) // len(l)
        ans = abs(sum([el - mean for el in l if el < mean]))
        print(ans)
    else:
        print(-1)
    
    n = int(input()) 