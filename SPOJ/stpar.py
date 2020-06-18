n = int(input())
while n:
    cur = 0
    st = []
    for c in list(map(int, input().split())):
        if c == cur + 1:
            cur += 1
            while len(st) and st[-1] == cur + 1:
                cur += 1
                st.pop()
        else:
            st.append(c)
    print(['no', 'yes'][cur == n])
    n = int(input())