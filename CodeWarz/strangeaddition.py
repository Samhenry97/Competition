#!/usr/bin/env python3
print('\n'.join([(lambda line: (lambda data: str(sum(data) + len(data)))(list(map(int, line.split()))))(line) for line in open(__import__('sys').argv[1], 'r')]), end='')