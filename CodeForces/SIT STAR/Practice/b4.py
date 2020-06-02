n = int(input())
ans = n // 100
n %= 100
ans += n // 10
n %= 10
print(ans + n)