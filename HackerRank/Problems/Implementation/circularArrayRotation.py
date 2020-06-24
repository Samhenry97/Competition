n, k, q = map(int, input().split())
l = list(map(int, input().split()))
for _ in range(q):
    m = int(input())
    print(l[(n - (k % n) + m) % n])