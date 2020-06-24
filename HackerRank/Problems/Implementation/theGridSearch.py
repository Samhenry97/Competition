def find(text, pat):
    n, m, ln, lm = len(text), len(text[0]), len(pat), len(pat[0])
    for y in range(n-ln+1):
        for x in range(m-lm+1):
            valid = True
            for yy in range(ln):
                if not valid: break
                for xx in range(lm):
                    if text[y+yy][x+xx] != pat[yy][xx]:
                        valid = False
                        break
            if valid: return True
    return False

for _ in range(int(input())):
    n, m = map(int, input().split())
    text = [input() for _ in range(n)]
    ln, lm = map(int, input().split())
    pat = [input() for _ in range(ln)]
    print(['NO', 'YES'][find(text, pat, )])