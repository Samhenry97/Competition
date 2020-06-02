n, m = map(int, input().split())
bad = []
for i in range(m):
    a, b = input().split()
    bad.append((ord(a) - ord('A'), ord(b) - ord('A')))
ans = 0
for i in range(1<<n):
    sel = [c == '1' for c in bin(i)[2:][::-1]]
    valid = True
    for a, b in bad:
        if a < len(sel) and b < len(sel) and sel[a] and sel[b]:
            valid = False
    if valid:
        ans = max(ans, sel.count(True))
print(ans)