n = int(input())
print(4 + n * 3)
print(0, 0)
print(1, 0)
for i in range(n+1):
    for j in range(3):
        if i == n and j == 2:
            break
        print(i+j, i+1)
