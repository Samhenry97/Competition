for _ in range(int(input())):
    n = int(input())
    ans = 0
    for i in range(len(bin(n)[2:])):
        ans += n // (2 ** i)
    print(ans)