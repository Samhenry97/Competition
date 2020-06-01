#!/usr/bin/env python3

print(''.join(list(map(lambda x: chr(int(x)), open(__import__('sys').argv[1], 'r').read().split()))), end='')
