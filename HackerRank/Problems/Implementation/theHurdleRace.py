n, k = map(int, input().split())
print(max(max(list(map(int, input().split()))) - k, 0))