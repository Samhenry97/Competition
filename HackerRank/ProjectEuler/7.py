MAXN = 120000

sieve = [False, False] + [True] * MAXN
p = 2
while p * p < MAXN:
    if sieve[p]:
        for i in range(p*p, MAXN, p):
            sieve[i] = False
    p += 1

prime = [i for i in range(MAXN) if sieve[i]]
for _ in range(int(input())):
    print(prime[int(input())-1])