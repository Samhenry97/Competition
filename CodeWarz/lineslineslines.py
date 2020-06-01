#!/usr/bin/env python3
print(' '.join(open(__import__('sys').argv[1], 'r').read().replace('\n', ' ').split()), end='')
