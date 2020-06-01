n = int(input())

while n != -1:
    final = []
    for i in range(n):
        if sum(list(map(int, input().split()))) <= 2:
            final.append(str(i))
    print(' '.join(final))

    n = int(input())
