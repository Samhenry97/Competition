for _ in range(int(input())):
    a, b, c = map(int, input().split())
    aa, ab = -1, -1
    if a < c:
        aa = 1
    if c < a * b:
        ab = b
    print(aa, ab)