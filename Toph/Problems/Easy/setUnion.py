input()
s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))
print(*sorted(list(s1 | s2)))