n = int(input())
fact = [1]
for i in range(2, 19):
    fact.append(i * fact[i-2])
if n <= 19:
    print(str(fact[n-1])[-4:])
else:
    print('0000')