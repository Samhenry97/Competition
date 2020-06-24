name = ['blah', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty']
for i in range(10):
    name.append('twenty ' + name[i + 1])
        
h, m = int(input()), int(input())
if m == 0:
    print('{} o\' clock'.format(name[h]))
elif m == 15:
    print('quarter past {}'.format(name[h]))
elif m == 30:
    print('half past {}'.format(name[h]))
elif m == 45:
    print('quarter to {}'.format(name[h + 1 if h < 12 else 1]))
elif m < 30:
    print('{} minute{} past {}'.format(name[m], '' if m == 1 else 's', name[h]))
else:
    print('{} minutes to {}'.format(name[60 - m], name[h + 1 if h < 12 else 1]))