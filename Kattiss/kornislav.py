l = list(map(int, input().split()))

l.remove(max(l))

first = max(l)
l.remove(first)

l.remove(max(l))

second = l[0]

print(first * second)
