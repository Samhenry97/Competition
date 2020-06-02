n = int(input())
l = list(map(int, input().split()))
ans = [-1] * n
avail = list(range(n))

def find(x):
    global avail
    for i in range(len(avail)-1, -1, -1):
        if avail[i] <= x:
            return i
    return -1

def place(i):
    global avail, ans, n, l
    if i == n:
        if ans < l:
            print(*ans)
            exit(0)
        return

    v = find(l[i])
    if avail[v] == l[i]:
        ans[i] = avail[v]
        avail.pop(v)
        place(i+1)
        avail.insert(v, ans[i])
        v -= 1
    if v != -1:
        ans[i] = avail[v]
        avail.pop(v)
        ans = ans[:i+1] + avail[::-1]
        print(*ans)
        exit(0)
place(0)
print(-1)