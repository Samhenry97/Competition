n = int(input())
ans = (n * (n+1))//2
for _ in range(int(input())):
    ans -= int(input())
print(ans)