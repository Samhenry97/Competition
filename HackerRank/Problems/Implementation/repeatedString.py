s = input()
n = int(input())
a = s.count('a')
print(a * (n // len(s)) + s[:n % len(s)].count('a'))