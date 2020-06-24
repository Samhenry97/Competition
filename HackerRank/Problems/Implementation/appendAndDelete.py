s = input()
t = input()
k = int(input())
i = 0
while i < len(s) and i < len(t) and s[i] == t[i]: i += 1
l = len(s) + len(t)
print(["No", "Yes"][l <= k + i * 2 and l % 2 == k % 2 or l < k])