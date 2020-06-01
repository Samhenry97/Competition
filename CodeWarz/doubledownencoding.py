#!/usr/bin/env python3

print((lambda data: ''.join([chr(int(data[x:x+2], 16) // 2) for x in range(0, len(data), 2)]))(open(__import__('sys').argv[1], 'r').read().strip()), end='')