t = int(input())

for _ in range(t):
    input()
    s = list(map(int, input().split()))
    print((max(s) - min(s)) * 2)
    
