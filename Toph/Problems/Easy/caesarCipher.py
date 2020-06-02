n = int(input())
s = input()
ans = []
for c in s:
    if c == ' ':
        ans.append(' ')
        continue
    loc = ord(c) - ord('a') - n
    if loc < 0:
        loc += 26
    ans.append(chr(loc + ord('a')))
print(''.join(ans))