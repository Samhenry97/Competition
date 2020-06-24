n, k = map(int, input().split())
l = list(map(int, input().split()))
cost = int(input())
correct = sum([l[x] for x in range(len(l)) if x != k]) // 2
if cost == correct:
    print('Bon Appetit')
else:
    print(cost - correct)