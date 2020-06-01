#!/usr/bin/env python3
print(''.join([chr(int(x, 16)) for x in open(__import__('sys').argv[1], 'r').read().split()]), end='')