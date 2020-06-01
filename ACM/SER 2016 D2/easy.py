let, num = input.split()
words = []
for i in range(int(num)):
  words.append(input())
pairs = []
for i in range(len(words) - 1):
    pairs.append((words[i], words[i+1]))
alphabet = []
for i in pairs:
    let1 = i[0][0]
    let2 = i[1][1]
    if let1 not in alphabet:
        alphabet.append(let1)
    if let2 not in alphabet:
        alphabet.append(let2)
    else:
        ord1 = alphabet.index(let1)
        ord2 = alphabet.index(let2)
        if(ord1 > ord2):
            print(1)
            exit()
