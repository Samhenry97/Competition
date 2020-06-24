h = list(map(int, input().split()))
s = input()
max = -1
for c in s:
    if h[ord(c) - ord('a')] > max:
        max = h[ord(c) - ord('a')]
print((len(s)) * max)