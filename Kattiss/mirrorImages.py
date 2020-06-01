t = int(input())

for _ in range(t):
    print("Test " + str(_ + 1))
    r, c = map(int, input().split())
    s = ''
    for _ in range(r):
        s += input()
    s = s[::-1]
    chunks, chunk_size = len(s), len(s) // r
    l = [ s[i:i + chunk_size] for i in range(0, chunks, chunk_size) ]
    for _ in range(len(l)):
        print(l[_])
