a, b = map(float, input().split())
print('{:.2f}'.format(b - a - 0.5) if b >= a + 0.5 and a % 5 == 0 else '{:.2f}'.format(b))