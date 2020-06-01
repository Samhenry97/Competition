t = int(input())
for _ in range(t):
    s = input()
    maxBits = 0
    for i in range(0, len(s)):
        temp = bin(int(s[0:i+1])).count('1')
        if(temp > maxBits):
            maxBits = temp
    print(maxBits)
