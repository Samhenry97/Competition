for _ in range(int(input())):
    s, k = input(), int(input())
    ans = []
    for c in s:
        if c == '0' and k:
            ans.append('1')
            k -= 1
        else:
            ans.append('0')
    print(''.join(ans))