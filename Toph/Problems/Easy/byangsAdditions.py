a, b = input().split()
a, b = a[::-1], b[::-1]
carry = False
for i in range(min(len(a), len(b))):
    tmp = int(a[i]) + int(b[i])
    if tmp >= 10:
        print('Yes')
        exit(0)
print('No')