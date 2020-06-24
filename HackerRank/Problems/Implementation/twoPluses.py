n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]

taken = set()

# Current test valid
def valid(s, oy, ox, taken):
    if len(taken) == 0:
        if grid[oy][ox] == 'B': return False
        taken.add((oy, ox))
        for i in range(1, s // 2 + 1):
            if grid[oy][ox - i] == 'B' or grid[oy][ox + i] == 'B':
                return False
            taken.add((oy, ox - i))
            taken.add((oy, ox + i))
            if grid[oy - i][ox] == 'B' or grid[oy + i][ox] == 'B':
                return False
            taken.add((oy - i, ox))
            taken.add((oy + i, ox))
    else:
        if grid[oy][ox] == 'B' or (oy, ox) in taken: return False
        for i in range(1, s // 2 + 1):
            if grid[oy][ox - i] == 'B' or grid[oy][ox + i] == 'B' or (oy, ox - i) in taken or (oy, ox + i) in taken:
                return False
            if grid[oy - i][ox] == 'B' or grid[oy + i][ox] == 'B' or (oy - i, ox) in taken or (oy + i, ox) in taken:
                return False
    return True

# Generate sizes
sizes = []
maxSize = min(n, m) - 1 if min(n, m) % 2 == 0 else min(n, m)
for y in range(1, maxSize + 1, 2):
    for x in range(y, maxSize + 1, 2):
        sizes.append((y, x))
sizes.sort(reverse=True, key=lambda x: x[0] * x[1])

for c in range(len(sizes)):
    s = sizes[c][0]
    for y in range(s // 2, n - s // 2):
        for x in range(s // 2, m - s // 2):
            if valid(s, y, x, taken):
                ss = sizes[c][1]
                for yy in range(ss // 2, n - ss // 2):
                    for xx in range(ss // 2, m - ss // 2):
                        if valid(ss, yy, xx, taken):
                            print((s // 2 * 4 + 1) * (ss // 2 * 4 + 1))
                            exit()            
            taken.clear()