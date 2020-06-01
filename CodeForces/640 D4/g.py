seq = [1, 3, 5, 2, 4, 6, 8, 10, 7, 9]
after = [
    [1],
    [1, 'l', 2],
    [1, 3, 'l', 2],
    [1, 3, 'l', 2, 4],
    [1, 3, 5, 2, 4],
    [1, 3, 5, 2, 4, 6],
    [1, 5, 2, 6, 3, 7, 4],
    [1, 5, 2, 6, 3, 7, 4, 8],
    [1, 3, 5, 2, 4, 7, 9, 6, 8]
]
base = [
    [-1],
    [-1],
    [-1],
    [2, 4, 1, 3],
    [1, 3, 5, 2, 4],
    [1, 3, 5, 2, 4, 6],
    [1, 5, 2, 6, 3, 7, 4],
    [1, 5, 2, 6, 3, 7, 4, 8],
    [1, 3, 5, 2, 4, 7, 9, 6, 8]
]
    
def check(ans):
    for i in range(1, len(ans)):
        if not (2 <= abs(ans[i-1] - ans[i]) <= 4):
            print('EXCEPT', len(ans), ans)
            exit(0)
    
for _ in range(int(input())):
    n = int(input())
    ans = []
    left = n % 10
    start = 10 * (n // 10)
    if start == 0:
        # check(base[n-1])
        print(*base[n-1])
        continue
    for i in range(n - left):
        ans.append(seq[i % 10] + 10 * (i // 10))
    if left == 0:
        # check(ans)
        print(*ans)
        continue
    
    toadd = [start + x if x != 'l' else ans.pop() for x in after[left-1]]
    ans.extend(toadd)
    # check(ans)
    print(*ans)