t = int(input())

for _ in range(t):
    input()
    months = list(map(int, input().split()))

    total = 0
    day = 0
    for m in months:
        if m >= 13:
            day = (day + 12) % 7
            if day == 5:
                total += 1
            day = (day + m - 12) % 7
        else:
            day = (day + m) % 7
    print(total)
