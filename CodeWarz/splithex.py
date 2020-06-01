#!/usr/bin/env python3
print(''.join([chr(int(a+b, 16)) for a, b in zip(*[list(line.strip()) for line in open(__import__('sys').argv[1], 'r')])]), end='')
