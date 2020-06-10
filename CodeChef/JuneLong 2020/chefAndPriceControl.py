for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for p in a:
        ans += p - k if p > k else 0
    print(ans)