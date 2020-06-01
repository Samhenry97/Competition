import sys
from random import randint

DEBUG = False

nums = ['101101']
tc = True
tn = True
ti = 0
tq = 0

def trollPrint(q, s):
    global tc, tq, ti, tn
    s = s.replace(' ', '')
    if q == 'Q':
        tq = 0
        for i in range(len(nums[ti])):
            if nums[ti][i] == s[i]:
                tq += 1
    else:
        print('Your answer: {}'.format(s))
        print('{} CORRECT'.format(nums[ti]) if s == nums[ti] else '{} WRONG'.format(nums[ti]))
        ti += 1
        tn = True

def trollInput():
    global tc, tq, ti, tn
    if tc:
        tc = False
        return len(nums)
    elif tn:
        tn = False
        return len(nums[ti])
    return tq


###############################################
###############################################
###############################################

def p(q, s):
    if DEBUG:
        trollPrint(q, s)
    else:
        print(q, s)
        sys.stdout.flush()
    
def inp():
    if DEBUG:
        return trollInput()
    else:
        return int(input())

Q, A = 'Q', 'A'

for _ in range(inp()):
    n = inp()
    ans = ['0'] * n
    p(Q, ' '.join(ans))
    zero = inp()
    
    idx = 0
    for i in range(0, n, 2):
        p(Q, ' '.join(list('0'*i + '11' + '0'*(n-i-2))))
        g = inp()
        if g == zero + 2:
            ans[i] = '1'
            ans[i + 1] = '1'
        elif g != zero - 2:
            p(Q, ' '.join(list('0'*i + '1' + '0'*(n-i-1))))
            g = inp()
            if g == zero + 1:
                ans[i] = '1'
            else:
                ans[i + 1] = '1'
        
    if n & 1: # Odd
        p(Q, ' '.join(list('0'*(n-1) + '1')))
        g = inp()
        if g == zero + 1:
            ans[i] = '1'
            
    p(A, ' '.join(ans))