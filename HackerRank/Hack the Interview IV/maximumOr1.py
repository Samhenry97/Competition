MOD = 1000000007

def below(n, k):
    sz = len(n)
    dp = [[[0 for _ in range(k+2)] for _ in range(2)] for _ in range(sz+1)]
    dp[0][0][0] = 1
    for i in range(sz):
        sm = 0
        while sm < 2:
            for j in range(k+1):
                x = 0
                v = ord(n[i]) - ord('0')
                while x <= (9 if sm else v):
                    dp[i+1][sm or x < v][j + (x > 0)] += dp[i][sm][j]
                    x += 1
            sm += 1
    return dp[sz][0][k] + dp[sz][1][k]

l, r, k = input(), input(), int(input())
bl = below(l, k)
br = below(r, k)
print((br - bl) % MOD)