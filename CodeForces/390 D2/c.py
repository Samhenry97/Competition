import re

uname = re.compile(r"[a-zA-Z0-9]+")

for _ in range(int(input())):
    input()
    users = set(input().split())
    messages = [input().split(":") for _ in range(int(input()))]
    for i, (u, m) in enumerate(messages):
        allowed = set()
        if u == "?":
            allowed = users.copy()
            for s in uname.findall(m):
                if s in users:
                    allowed.discard(s)
        messages[i].append(allowed)
    good = True
    for i, (u, m, a) in enumerate(messages):
        if u == "?":
            if i > 0:
                a.discard(messages[i-1][0])
            if i < len(messages) - 1:
                a.discard(messages[i+1][0])
            if len(a) == 0:
                good = False
                break
            messages[i][0] = list(a)[0]
    if good:
        for u, m, a in messages:
            print(f"{u}:{m}")
    else:
        print("Impossible")
        