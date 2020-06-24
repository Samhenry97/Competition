likes = 0
p = 5
for _ in range(int(input())):
    likes += p // 2
    p = (p // 2) * 3
print(likes)