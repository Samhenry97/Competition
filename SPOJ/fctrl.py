for _ in range(int(input())):
    n = int(input())
    five = 5 ** 20
    total = 0
    while five >= 5:
        total += n // five
        five = five // 5
    print(total) 