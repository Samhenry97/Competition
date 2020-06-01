t = int(input())

for _ in range(t):
    step, s = input().split()

    p, q = map(int, s.split('/'))

    dirs = []
    while p != 1 or q != 1:
        if p > q:
            p = p - q
            dirs.append(-1)
        else:
            q = q - p
            dirs.append(1)

    banana = 1
    for i in dirs[::-1]:
        if i == -1:
            banana = banana * 2
        else:
            banana = banana * 2 - 1

    print(step, 2 ** (len(dirs)) + banana - 1)
