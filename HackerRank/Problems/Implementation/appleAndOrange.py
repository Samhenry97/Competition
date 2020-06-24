s, t = map(int, input().split())
a, b = map(int, input().split())
m, n = map(int, input().split())
apple = list(map(int, input().split()))
orange = list(map(int, input().split()))

print(sum([1 for x in apple if (x + a) >= s and (x + a) <= t]))
print(sum([1 for x in orange if (x + b) >= s and (x + b) <= t]))