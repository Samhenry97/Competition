INF=10**20
    
n = int(input())
a = list(map(int, input().split()))
end = 0
ans = 0
curmax = -INF
for num in a:
    end += num
    curmax = max(curmax, num)
    ans = max(ans, end-curmax)
    if end < 0:
        end = 0
        curmax = -INF
print(ans)