t = int(input())

for i in range(t):
    num, source, target = input().split()
    n = 0
    for c in num:
        n = n * len(source) + source.find(c)

    result = ''
    while n:
        result = target[n % len(target)] + result
        n //= len(target)
    print('Case #' + str(i+1) + ': ' + result)
