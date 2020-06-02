input()
l = list(map(int, input().split()))
print(['No', 'Yes'][sorted(l) == l])