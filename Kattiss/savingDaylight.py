while True:
    try:
        s = input().split()
        hours = int(s[4].split(':')[0]) - int(s[3].split(':')[0])
        minutes = int(s[4].split(':')[1]) - int(s[3].split(':')[1])
        while minutes < 0:
            minutes += 60
            hours -= 1

        print(s[0], s[1], s[2], hours, "hours", minutes, "minutes")
    except EOFError:
        break
