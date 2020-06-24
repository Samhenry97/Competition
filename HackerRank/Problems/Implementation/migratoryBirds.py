count = [0] * 5
input()
for el in list(map(int, input().split())):
    count[el - 1] += 1
print(count.index(max(count)) + 1)