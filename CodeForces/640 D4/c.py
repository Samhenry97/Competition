for _ in range(int(input())):
    n, k = map(int, input().split())
    bot, top = 0, 10000000000
    mid = (bot + top) // 2
    while top - bot > 0:
        tmp = mid - mid // n
        if tmp == k:
            if mid % n == 0:
                print(mid-1)
            else:
                print(mid)
            break
        elif tmp < k:
            bot = mid
        else:
            top = mid
        mid = (bot + top) // 2