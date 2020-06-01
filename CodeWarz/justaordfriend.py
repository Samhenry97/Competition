#!/usr/bin/env python3
print(sum([ord(c) for c in open(__import__('sys').argv[1], 'r').read().replace('\n', '') if c.isalpha()]), end='')
