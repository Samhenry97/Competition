for _ in range(int(input())):
    input()
    change = { 5: 0, 10: 0, 15: 0 }
    valid = True
    for coin in list(map(int, input().split())):
        due = coin - 5
        if due == 5:
            if change[5] > 0:
                change[5] -= 1
            else:
                valid = False
                break
        elif due == 10:
            if change[10] > 0:
                change[10] -= 1
            elif change[5] > 1:
                change[5] -= 2
            else:
                valid = False
                break
        change[coin] += 1
    print(['NO', 'YES'][valid])