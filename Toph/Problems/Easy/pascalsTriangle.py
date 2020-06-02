r = [1]
for i in range(int(input())-1):
    rn = [1] * (len(r)+1)
    for j in range(1, len(r)):
        rn[j] = r[j] + r[j-1]
    r = rn
print(sum(r))