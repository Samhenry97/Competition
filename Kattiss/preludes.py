map1 = { 'A':'UNIQUE', 'A#':'Bb', 'Bb':'A#', 'B':'UNIQUE', 'C':'UNIQUE', 'C#':'Db', 'Db':'C#', 'D':'UNIQUE', 'D#':'Eb', 'Eb':'D#', 'E':'UNIQUE', 'F':'UNIQUE', 'F#':'Gb', 'Gb':'F#', 'Ab':'G#', 'G#':'Ab', 'G':'UNIQUE' }

step = 1
while True:
    try:
        s = input().split()
        print("Case " + str(step) + ": " + map1[s[0]] + ("" if map1[s[0]] == 'UNIQUE' else (" " + s[1])))
        step += 1
    except EOFError:
        break
