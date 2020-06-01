d = { 'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '_': '..--', ',': '.-.-', '.': '---.', '?': '----' }
inv_map = {v: k for k, v in d.items()}

while True:
    try:
        morse = []
        lens = []

        s = input()
        for c in s:
            morse.append(d[c])
            lens.append(str(len(d[c])))

        morse = ''.join(morse)
        lens.reverse()


        cursor = 0
        final = []
        for i in lens:
            i = int(i)
            final.append(inv_map[morse[cursor:cursor + i]])
            cursor += i

        print(''.join(final))
    except EOFError:
        break
