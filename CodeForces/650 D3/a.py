for _ in range(int(input())):
    s = input()
    ans = []
    for i in range(0, len(s), 2):
        ans.append(s[i])
    ans.append(s[-1])
    print(''.join(ans))