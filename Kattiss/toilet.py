s = input()

p1 = p2 = p3 = 0
s1 = s2 = s3 = s[0]

for i in range(1, len(s)):
    p1 += s1 != s[i]
    p2 += s2 != s[i]
    p3 += s3 != s[i]

    s1 = s2 = s3 = s[i]

    p1 += s1 != 'U'
    p2 += s2 != 'D'

    s1 = 'U'
    s2 = 'D'
        
print(p1, p2, p3, sep='\n')
