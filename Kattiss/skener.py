r, c, zr, zc = map(int, input().split())

for _ in range(r):
    s = input()
    finalStr = ''
    for c in s:
        finalStr += c * zc
    for _ in range(zr):
        print(finalStr)
        
