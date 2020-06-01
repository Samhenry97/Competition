while True:
    try:
        s = input().split()
        time1 = int(s[3].split(':')[0]) * 100 + int(s[3].split(':')[1])
        time2 = int(s[4].split(':')[0]) * 100 + int(s[4].split(':')[1])
        if time2 < time1:
            time2 = time2 + 2360
        diff = time2 - time1
        hours = diff // 100
        minutes = diff % 100
        hours += minutes // 60
        minutes = minutes % 60
        print(s[0], s[1], s[2], hours, "hours", minutes, "minutes")
    except EOFError:
        break
