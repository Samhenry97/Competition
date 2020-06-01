#!/usr/bin/env python3

num = int(open(__import__('sys').argv[1], 'r').read())
ans = [num + 3]
ans.append(num + 4)
ans.append(num + 7)
ans.append(num + 10)
ans.append(num + 17)
print(' '.join([str(x) for x in ans]), end='')