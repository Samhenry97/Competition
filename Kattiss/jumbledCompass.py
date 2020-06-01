n = int(input())
k = int(input())

ans = abs(n - k)

if ans < 360 - ans:
    if n > k and abs(n - k) > 180:
        print(ans)
    elif n > k and abs(n - k) < 180:
        print(-ans)
    elif n < k and abs(n - k) > 180:
        print(-ans)
    else:
        print(ans)
else:
    if n > k and abs(n - k) > 180:
        print(360 - ans)
    elif n > k and abs(n - k) < 180:
        print(-(360 - ans))
    elif n < k and abs(n - k) > 180:
        print(-(360 - ans))
    else:
        print(360 - ans)
