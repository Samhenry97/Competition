n, k =  map(int, input().split())
a = list(map(int, input().split()))
page = 0
ans = 0
for cnt in a:
    for prob in range(cnt):
        if prob % k == 0:
            page += 1
        if prob == page - 1:
            ans += 1
print(ans)