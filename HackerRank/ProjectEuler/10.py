from bisect import bisect

MAXN = 1000000

sieve = [False, False] + [True] * MAXN
p = 2
while p * p < MAXN:
    if sieve[p]:
        for i in range(p*p, MAXN, p):
            sieve[i] = False
    p += 1

prime = [i for i in range(MAXN) if sieve[i]]
sprime = [prime[0]]
for i in range(1, len(prime)):
    sprime.append(sprime[-1] + prime[i])

for _ in range(int(input())):
    print(sprime[bisect(prime, int(input()))-1])