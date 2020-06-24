l = []
input()
for tmp in map(int, input().split()):
    if len(l) == 0 or l[-1] != tmp:
        l.append(tmp)
input()
for tmp in map(int, input().split()):
    while len(l) > 0 and tmp >= l[-1]:
        l.pop()
    print(len(l) + 1)