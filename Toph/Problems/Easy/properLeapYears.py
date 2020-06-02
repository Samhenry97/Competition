y = int(input())
print(['No', 'Yes'][y % 4 == 0 and (y % 400 == 0 or y % 100 != 0)])