while True:
    try:
        l = input().split()
        if len(l) == 0:
            continue

        name = ''
        total = 0
        sumTotal = 0
        for s in l:
            try:
                n = float(s)
                total += 1
                sumTotal += n
            except:
                name += s + ' '
        print(sumTotal / total, name[:-1])
    except EOFError:
        break

