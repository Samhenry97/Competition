a = {}
h = []
for _ in range(int(input())):
    d = eval(input())
    cite = int(d['citing_paper_count'])
    for author in d['authors']['authors']:
        name = author['full_name']
        if name in a:
            a[name].append(cite)
        else:
            a[name] = [cite]
    
        
for name, l in a.items():
    tmp = sorted(a[name], reverse=True)
    h.append([1, name])
    found = False
    for i, num in enumerate(tmp):
        if i >= num:
            h[-1][0] = i
            found = True
            break
    if not found:
        h[-1][0] = len(tmp)

h.sort(reverse=True)
cur = h[0][0]
tmp = []
for author in h:
    if author[0] == cur:
        tmp.append(author)
    else:
        tmp.sort(key=lambda x: x[1])
        for item in tmp:
            print(item[1], item[0])
        tmp = [author]
        cur = author[0]

tmp.sort(key=lambda x: x[1])
for item in tmp:
    print(item[1], item[0])